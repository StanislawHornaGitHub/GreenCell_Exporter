from src.GreenCell.API import GreenCell


class HealthCheck:

    @staticmethod
    def get() -> str:
        return {
            "logged_in": GreenCell.is_logged_in(),
        }
