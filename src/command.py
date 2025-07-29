class Command:
    UNKNOWN = "unknown"
    UPDATE_TRACKING = "update_tracking"
    STOP_TRACKING = "stop_tracking"
    REBOOT_SERVER = "reboot_server"
    DISCONNECT = "disconnect"
    START_STREAM = "start_stream"
    STOP_STREAM = "stop_stream"
    CHANGE_STREAM_RES = "change_stream_res"
    TRACKER_DATA = "tracker_data"
    SEND_CFS = "send_cfs"
    REQUEST_TRACKING = "request_tracking"
    START_TRANSMISSION = "start_transmission"
    STOP_TRANSMISSION = "stop_transmission"

    ## Server UI Commands
    TOGGLE_ROI = "toggle_roi"
    TOGGLE_CROSSHAIR = "toggle_crosshair"