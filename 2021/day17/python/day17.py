import sys

class trajectory:
    def __init__(self, target_x, target_y):
        #want to define ranges with the lowest value first
        self.x_range = (min(target_x), max(target_x))
        self.y_range = (min(target_y), max(target_y))

    #specify origin, x velocity and y velocity
    #trace designed to stop once target area is unreachable.
    def trace(self, origin, vx, vy):
        x, y = origin
        apex = y

        #quite arbitrary definitions:
        while x <= self.x_range[1] and y >= self.y_range[0]:
            xprev = x
            yprev = y
            if y > apex:
                apex = y
            x += vx
            y += vy
            if vx > 0:
                vx -= 1
            vy -= 1

        if self.x_range[0] <= xprev <= self.x_range[1] and self.y_range[0] <= yprev <= self.y_range[1]:
            return True, apex
        else:
            return False, None

    def valid_traces(self):
        #valid x values constitute a range between:
        # upper: the highest value of the range of the target area
        # lower: (not implemented)

        #valid y values constitute a range between:
        # upper: -1*lowest y
        # lower: lowest value of y range

        trajectories = []
        for vx in range(self.x_range[1]+1):
            for vy in range(self.y_range[0], -1*self.y_range[0]+1):
                hit, apex = self.trace((0,0), vx, vy)
                if hit:
                    trajectories.append([(vx, vy), apex])
                vy += 1

        highest = max(traj[1] for traj in trajectories)

        return highest, len(trajectories)

if __name__ == "__main__":
    probe = trajectory((20, 30), (-10, -5))
    print(probe.valid_traces())

    probe = trajectory((137, 171), (-98, -73))
    print(probe.valid_traces())