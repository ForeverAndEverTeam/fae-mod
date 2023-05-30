init -999 python:

    from pypresence import Presence
    import time

    def setupRPC(status=None):

        client_id = '966384640489295964'  # Fake ID, put your real one here
        RPC = Presence(client_id)  # Initialize the client class
        RPC.connect() # Start the handshake loop

        if status is None:
            raise Exception("Must provide status")

        print(RPC.update(state=status, large_image='faelogo', details="Spending Time With Sayori", start=time.time(), large_text="Forever & Ever"))  # Set the presence