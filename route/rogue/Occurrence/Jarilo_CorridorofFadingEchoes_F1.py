from tasks.map.control.waypoint import Waypoint
from tasks.map.keywords.plane import Jarilo_CorridorofFadingEchoes
from tasks.rogue.route.base import RouteBase


class Route(RouteBase):

    def Jarilo_CorridorofFadingEchoes_F1_X236Y903(self):
        """
        | Waypoint | Position                  | Direction | Rotation |
        | -------- | ------------------------- | --------- | -------- |
        | spawn    | Waypoint((236.6, 903.4)), | 274.2     | 274      |
        | event    | Waypoint((278.4, 972.0)), | 289.1     | 290      |
        | exit     | Waypoint((169.2, 904.0)), | 261.8     | 269      |
        """
        self.map_init(plane=Jarilo_CorridorofFadingEchoes, floor="F1", position=(236.6, 903.4))
        self.register_domain_exit(Waypoint((169.2, 904.0)), end_rotation=269)
        event = Waypoint((278.4, 972.0))

        self.clear_event(event)
        # ===== End of generated waypoints =====

    def Jarilo_CorridorofFadingEchoes_F1_X265Y963(self):
        """
        | Waypoint | Position                   | Direction | Rotation |
        | -------- | -------------------------- | --------- | -------- |
        | spawn    | Waypoint((265.5, 963.6)),  | 233.8     | 230      |
        | item     | Waypoint((250.1, 970.4)),  | 157.2     | 244      |
        | event    | Waypoint((231.8, 991.0)),  | 233.9     | 230      |
        | exit     | Waypoint((227.6, 1000.4)), | 229.9     | 228      |
        """
        self.map_init(plane=Jarilo_CorridorofFadingEchoes, floor="F1", position=(265.5, 963.6))
        self.register_domain_exit(Waypoint((227.6, 1000.4)), end_rotation=228)
        item = Waypoint((250.1, 970.4))
        event = Waypoint((231.8, 991.0))

        self.clear_item(item)
        self.clear_event(event)
        # ===== End of generated waypoints =====
