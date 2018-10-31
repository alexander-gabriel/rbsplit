import Tkinter as tk
from datetime import datetime
from db import DB
from ros import Ros

class GUI:
    def __init__(self):
        self.db = DB()
        self.last_timestamp = datetime.fromtimestamp(self.db.get_last_timestamp()[0] or 0.0)
        self.current_timestamp = self.last_timestamp
        for entry in self.db.get_entries():
            print(entry)
        self.root = tk.Tk()
        button = tk.Button(self.root, text='add Timestamp', width=25, command=self.timestamp_callback)
        button.grid(column=1, row=1)
        text = tk.Text(self.root, height=1, width=40)
        text.insert(tk.END, "Last Timestamp: " + self.last_timestamp.strftime("%s"))
        text.grid(column=1, row=2)
        button = tk.Button(self.root, text='distance:  5', width=25, command=self.distance5_callback)
        button.grid(column=1, row=3)
        button = tk.Button(self.root, text='distance: 10', width=25, command=self.distance10_callback)
        button.grid(column=1, row=4)
        button = tk.Button(self.root, text='distance: 15', width=25, command=self.distance15_callback)
        button.grid(column=1, row=5)
        button = tk.Button(self.root, text='distance: 20', width=25, command=self.distance20_callback)
        button.grid(column=1, row=6)
        button = tk.Button(self.root, text='distance: 25', width=25, command=self.distance25_callback)
        button.grid(column=1, row=7)
        button = tk.Button(self.root, text='distance: 30', width=25, command=self.distance30_callback)
        button.grid(column=1, row=8)
        button = tk.Button(self.root, text='distance: 35', width=25, command=self.distance35_callback)
        button.grid(column=1, row=9)
        button = tk.Button(self.root, text='distance: 40', width=25, command=self.distance40_callback)
        button.grid(column=1, row=10)
        button = tk.Button(self.root, text='distance: 45', width=25, command=self.distance45_callback)
        button.grid(column=1, row=11)
        button = tk.Button(self.root, text='distance: 50', width=25, command=self.distance50_callback)
        button.grid(column=1, row=12)
        button = tk.Button(self.root, text='walking away', width=25, command=self.walk_away_callback)
        button.grid(column=2, row=1)
        button = tk.Button(self.root, text='walking towards', width=25, command=self.walk_towards_callback)
        button.grid(column=2, row=2)
        button = tk.Button(self.root, text='walking right', width=25, command=self.walk_right_callback)
        button.grid(column=2, row=3)
        button = tk.Button(self.root, text='walking left', width=25, command=self.walk_left_callback)
        button.grid(column=2, row=4)
        button = tk.Button(self.root, text='walking away (crate)', width=25, command=self.walk_away_crate_callback)
        button.grid(column=3, row=1)
        button = tk.Button(self.root, text='walking towards (crate)', width=25, command=self.walk_towards_crate_callback)
        button.grid(column=3, row=2)
        button = tk.Button(self.root, text='walking right (crate)', width=25, command=self.walk_right_crate_callback)
        button.grid(column=3, row=3)
        button = tk.Button(self.root, text='walking left (crate)', width=25, command=self.walk_left_crate_callback)
        button.grid(column=3, row=4)
        button = tk.Button(self.root, text='crate down away', width=25, command=self.crate_down_away_callback)
        button.grid(column=4, row=1)
        button = tk.Button(self.root, text='crate down side', width=25, command=self.crate_down_side_callback)
        button.grid(column=4, row=2)
        button = tk.Button(self.root, text='crate down side (unhealthy)', width=25, command=self.crate_down_side_unhealthy_callback)
        button.grid(column=4, row=3)
        button = tk.Button(self.root, text='crate down towards', width=25, command=self.crate_down_towards_callback)
        button.grid(column=4, row=4)
        button = tk.Button(self.root, text='crate up away', width=25, command=self.crate_up_away_callback)
        button.grid(column=5, row=1)
        button = tk.Button(self.root, text='crate up side', width=25, command=self.crate_up_side_callback)
        button.grid(column=5, row=2)
        button = tk.Button(self.root, text='crate up side (unhealthy)', width=25, command=self.crate_up_side_unhealthy_callback)
        button.grid(column=5, row=3)
        button = tk.Button(self.root, text='crate up towards', width=25, command=self.crate_up_towards_callback)
        button.grid(column=5, row=4)
        button = tk.Button(self.root, text='gesture: wave', width=25, command=self.gesture_wave_callback)
        button.grid(column=6, row=1)
        button = tk.Button(self.root, text='gesture: come', width=25, command=self.gesture_come_callback)
        button.grid(column=6, row=2)
        button = tk.Button(self.root, text='gesture: shush', width=25, command=self.gesture_shush_callback)
        button.grid(column=6, row=3)
        button = tk.Button(self.root, text='gesture: stop', width=25, command=self.gesture_stop_callback)
        button.grid(column=6, row=4)
        button = tk.Button(self.root, text='gesture: thumbs up', width=25, command=self.gesture_thumbs_up_callback)
        button.grid(column=6, row=5)
        button = tk.Button(self.root, text='gesture: thumbs down', width=25, command=self.gesture_thumbs_down_callback)
        button.grid(column=6, row=6)
        button = tk.Button(self.root, text='gesture: arm up', width=25, command=self.gesture_arm_up_callback)
        button.grid(column=6, row=7)
        button = tk.Button(self.root, text='gesture: arm down', width=25, command=self.gesture_arm_down_callback)
        button.grid(column=6, row=8)
        button = tk.Button(self.root, text='pointing:   0', width=25, command=self.point0_callback)
        button.grid(column=7, row=1)
        button = tk.Button(self.root, text='pointing:  45', width=25, command=self.point45_callback)
        button.grid(column=7, row=2)
        button = tk.Button(self.root, text='pointing:  90', width=25, command=self.point90_callback)
        button.grid(column=7, row=3)
        button = tk.Button(self.root, text='pointing: 135', width=25, command=self.point135_callback)
        button.grid(column=7, row=4)
        button = tk.Button(self.root, text='pointing: 180', width=25, command=self.point180_callback)
        button.grid(column=7, row=5)
        button = tk.Button(self.root, text='pointing: 225', width=25, command=self.point225_callback)
        button.grid(column=7, row=6)
        button = tk.Button(self.root, text='pointing: 270', width=25, command=self.point270_callback)
        button.grid(column=7, row=7)
        button = tk.Button(self.root, text='pointing: 315', width=25, command=self.point315_callback)
        button.grid(column=7, row=8)

    def time_callback(self, msg):
        self.current_timestamp = datetime(second=msg.header.stamp.secs, microsecond=msgs.header.stamp.nsecs)

    def timestamp_callback(self):
        self.last_timestamp = self.current_timestamp
        self.db.add_timestamp(self.last_timestamp)

    def walk_away_callback(self):
        self.db.add_type(self.last_timestamp, "walk_away")

    def walk_towards_callback(self):
        self.db.add_type(self.last_timestamp, "walk_towards")

    def walk_right_callback(self):
        self.db.add_type(self.last_timestamp, "walk_right")

    def walk_left_callback(self):
        self.db.add_type(self.last_timestamp, "walk_left")

    def walk_away_crate_callback(self):
        self.db.add_type(self.last_timestamp, "walk_away_crate")

    def walk_towards_crate_callback(self):
        self.db.add_type(self.last_timestamp, "walk_towards_crate")

    def walk_right_crate_callback(self):
        self.db.add_type(self.last_timestamp, "walk_right_crate")

    def walk_left_crate_callback(self):
        self.db.add_type(self.last_timestamp, "walk_left_crate")

    def crate_down_away_callback(self):
        self.db.add_type(self.last_timestamp, "crate_down_away")

    def crate_down_side_callback(self):
        self.db.add_type(self.last_timestamp, "crate_down_side")

    def crate_down_side_unhealthy_callback(self):
        self.db.add_type(self.last_timestamp, "crate_down_side_unhealthy")

    def crate_down_towards_callback(self):
        self.db.add_type(self.last_timestamp, "crate_down_towards")

    def crate_up_away_callback(self):
        self.db.add_type(self.last_timestamp, "crate_up_away")

    def crate_up_side_callback(self):
        self.db.add_type(self.last_timestamp, "crate_up_side")

    def crate_up_side_unhealthy_callback(self):
        self.db.add_type(self.last_timestamp, "crate_up_side_unhealthy")

    def crate_up_towards_callback(self):
        self.db.add_type(self.last_timestamp, "crate_up_towards")

    def gesture_wave_callback(self):
        self.db.add_type(self.last_timestamp, "gesture_wave")

    def gesture_come_callback(self):
        self.db.add_type(self.last_timestamp, "gesture_come")

    def gesture_shush_callback(self):
        self.db.add_type(self.last_timestamp, "gesture_shush")

    def gesture_stop_callback(self):
        self.db.add_type(self.last_timestamp, "gesture_stop")

    def gesture_thumbs_up_callback(self):
        self.db.add_type(self.last_timestamp, "gesture_thumbs_up")

    def gesture_thumbs_down_callback(self):
        self.db.add_type(self.last_timestamp, "gesture_thumbs_down")

    def gesture_arm_up_callback(self):
        self.db.add_type(self.last_timestamp, "gesture_arm_up")

    def gesture_arm_down_callback(self):
        self.db.add_type(self.last_timestamp, "gesture_arm_down")

    def point0_callback(self):
        self.db.add_type(self.last_timestamp, "point_0")

    def point45_callback(self):
        self.db.add_type(self.last_timestamp, "point_45")

    def point90_callback(self):
        self.db.add_type(self.last_timestamp, "point_90")

    def point135_callback(self):
        self.db.add_type(self.last_timestamp, "point_135")

    def point180_callback(self):
        self.db.add_type(self.last_timestamp, "point_180")

    def point225_callback(self):
        self.db.add_type(self.last_timestamp, "point_225")

    def point270_callback(self):
        self.db.add_type(self.last_timestamp, "point_270")

    def point315_callback(self):
        self.db.add_type(self.last_timestamp, "point_315")

    def distance5_callback(self):
        self.db.add_distance(self.last_timestamp, 5)

    def distance10_callback(self):
        self.db.add_distance(self.last_timestamp, 10)

    def distance15_callback(self):
        self.db.add_distance(self.last_timestamp, 15)

    def distance20_callback(self):
        self.db.add_distance(self.last_timestamp, 20)

    def distance25_callback(self):
        self.db.add_distance(self.last_timestamp, 25)

    def distance30_callback(self):
        self.db.add_distance(self.last_timestamp, 30)

    def distance35_callback(self):
        self.db.add_distance(self.last_timestamp, 35)

    def distance40_callback(self):
        self.db.add_distance(self.last_timestamp, 40)

    def distance45_callback(self):
        self.db.add_distance(self.last_timestamp, 45)

    def distance50_callback(self):
        self.db.add_distance(self.last_timestamp, 50)

    def start(self):
        Ros(self.timestamp_callback)
        self.root.mainloop()
        self.db.close_db()
