def execute_system_command(command):
    import os
    # No permission check
    return os.system(command)
