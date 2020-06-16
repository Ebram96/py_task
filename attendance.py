"""
This contains the attendance interface for employees
"""
from datetime import datetime, timedelta


class Attendance:
    """Represents the interface needed for checking attendance"""
    def __init__(self, db):
        self.db = db

    def get_attendance(self, emp, day):
        """
        Returns the attendance for an employee in a give date and for how long.
        """
        result = {"attended": False}
        attended = self.db.query_data(
            table="Attendance", employee=emp, day=day
        )

        if attended:  # if there are entries in Attendance table for employee
            result["attended"] = True
            attendance_id = attended[0][0]
            # Grab all attendance actions from database and use datetime
            # objects to make date and time operations easier..
            actions = [
                {
                    "time": datetime.strptime(action[2], "%Y-%m-%d %I:%M %p"),
                    "type": action[3]
                }
                for action in self.db.query_data(
                    table="AttendanceActions", Attendanceid=attendance_id
                )
            ]
            duration = 0
            last_check_in = datetime.strptime(day, "%Y-%m-%d")
            # Calculate the duration in seconds
            for action in actions:
                if action["type"] == "CheckIn":
                    last_check_in = action["time"]
                else:
                    duration += (action["time"] - last_check_in).seconds

            # If there is a night shift overlapping with the next day..
            if actions[-1]["type"] == "CheckIn":
                duration += (
                    datetime.strptime(day, "%Y-%m-%d") + timedelta(days=1)
                    - actions[-1]["time"]
                ).seconds

            hours = duration // 3600
            minutes = (duration % 3600) // 60
            result["duration"] = f"{hours:02}:{minutes:02}"

        return result

    def get_history(self, emp):
        """Return an attendance history of an employee in UTC time"""
        user_attendance_ids = [
            x[0] for x in self.db.query_data(table="Attendance", employee=emp)
        ]
        actions = []
        for attendance_id in user_attendance_ids:
            actions.extend(
                self.db.query_data(
                    table="AttendanceActions", Attendanceid=attendance_id
                )
            )

        # Store action type and time (UTC) only
        actions = [
            (
                action[3],
                datetime.utcfromtimestamp(
                    datetime.strptime(
                        action[2], "%Y-%m-%d %I:%M %p"
                    ).timestamp()
                ),
            )
            for action in actions
        ]

        # Sort chronologically
        actions.sort(key=lambda tup: tup[1])

        result = {"days": []}
        day_actions = {}
        
        for action in actions:
            date = str(action[1].date())
            serialized_action = {
                "action": action[0],
                "time": action[1].isoformat()
            }
            if date in day_actions:
                day_actions[date].append(serialized_action)
            else:
                day_actions[date] = [serialized_action]
        
        for day, actions in day_actions.items():
            result["days"].append({"date": day, "actions": actions})

        return result
