init -750 python in fae_threading:

    import threading

    class FAEsyncWrapper(object):


        def __init__(self,
                async_fun,
                async_args=[],
                async_kwargs={}
            ):

            
            self._th_lock = threading.Lock()
            self._th_cond = threading.Condition(self._th_lock)
            self._th_result = None
            self._th_function = async_fun
            self._th_args = async_args
            self._th_kwargs = async_kwargs
            self._th_thread = None
            self._th_done = True
            self.ready = True

            # check for key things
            if (
                    self._th_function is None
                    or self._th_args is None
                    or self._th_kwargs is None
                ):
                self.ready = False


        def done(self):
            """
            Returns true if the thread is Done and has returned data, False
            otherwise.
            """
            if self.ready:
                return True

            is_done = False

            # lock and check
            self._th_cond.acquire()
            is_done = self._th_done
            self._th_cond.release()

            return is_done


        def end(self):
            """
            Resets thread status vars and more so we can spawn a new thread.

            Checks if the thread is done before doing any resets
            """
            if self.ready or not self.done():
                return

            # otherwise we can reset
            self.__end()


        def get(self):
            """
            Retrieves value set by thread and resets everything so we can
            spawn a new thread.

            RETURNS:
                value returned from async call.
                or None if the async call is still returning. (or if your
                    async call returned None)
            """
            # dont need to waste time here if we arent running anything
            if self.ready:
                return self._th_result

            # dont do anything if we arent done
            if not self.done():
                return None

            # otherwise we are DONE and we return the result
            ret_val = self._th_result
            self.__end()

            return ret_val


        def start(self):
            """
            Starts the threaded function call.
            """
            if not self.ready:
                return

            # otherwise time to make new thread I guess
            self._th_done = False
            self._th_result = None
            self.ready = False
            self._th_thread = threading.Thread(target=self._th_start)
            self._th_thread.start()


        def _th_start(self):
            """
            Actually runs the async function and sets the result var
            appropriately.
            """
            temp_result = self._th_function(*self._th_args, **self._th_kwargs)

            # acquire lock and set the result var
            self._th_cond.acquire()
            self._th_result = temp_result
            self._th_done = True
            self._th_cond.release()


        def __end(self):
            """
            Resets vars so we can spawn a new thred. Does NOT check if the
            thread is done.
            """
            self._th_result = None
            self._th_done = True
            self.ready = True