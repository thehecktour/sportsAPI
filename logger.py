class YatagarasuLogger:
    def __init__(self, level):
        self.level = level
        self.errors_levels = {
            "INFO": 10,
            "DEBUG": 20,
            "WARNING": 30,
            "EXCEPTION": 40,
            "ERROR": 50,
            "CRITICAL": 60
        }

    def set_level(self, level):
        self.level = level   

    def log_error(self, message):
        if self.errors_levels[self.level] >= self.errors_levels["ERROR"]:
            return f"ERROR: {message}"
    
    def log_debug(self, message):
        if self.errors_levels[self.level] >= self.errors_levels["DEBUG"]:
            return f"DEBUG: {message}"
    
    def log_info(self, message):
        if self.errors_levels[self.level] >= self.errors_levels["INFO"]:
            return f"INFO: {message}"

    def log_warning(self, message):
        if self.errors_levels[self.level] >= self.errors_levels["WARNING"]:
            return f"WARNING: {message}"
    
    def log_exception(self, message):
        if self.errors_levels[self.level] >= self.errors_levels["EXCEPTION"]:
            return f"EXCEPTION: {message}"
    
    def log_critical(self, message):
        if self.errors_levels[self.level] >= self.errors_levels["CRITICAL"]:
            return f"CRITICAL: {message}"
    
    def show_logs(self):
        return "\n".join(self.logs)

logger = YatagarasuLogger("DEBUG")
logger.set_level("DEBUG")
logger.show_logs()
