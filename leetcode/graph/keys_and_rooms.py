import typing
import collections


class Solution:
    def canVisitAllRooms(self, rooms: typing.List[typing.List[int]]) -> bool:
        visited = [False] * len(rooms)
        queue = collections.deque()

        keys = set()

        visited[0] = True

        for key in rooms[0]:
            queue.append(key)
            keys.add(key)

        while queue:
            front = queue.popleft()

            if visited[front]:
                continue

            visited[front] = True

            for child in rooms[front]:
                if child not in keys:
                    queue.append(child)
                    keys.add(child)

        return all(visited)



if __name__ == "__main__":
    s = Solution()

    rooms = [[1], [2], [3], []]
    assert s.canVisitAllRooms(rooms)

