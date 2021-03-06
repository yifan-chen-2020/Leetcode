from collections import deque

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        prerequisites_count_list = [0 for _ in range(numCourses)]
        next_courses = {i: [] for i in range(numCourses)}
        # prerequisites_count_list = []
        for pairs in prerequisites:
            post, pre = pairs
            next_courses[pre].append(post)
            prerequisites_count_list[post] += 1

        course_queue = deque([])
        course_order = []
        count = 0

        for i, pre_list in enumerate(prerequisites_count_list):
            if pre_list == 0:
                course_queue.append(i)
                course_order.append(i)

        while course_queue:
            completed_course = course_queue.popleft()
            count += 1

            for next_course in next_courses[completed_course]:
                prerequisites_count_list[next_course] -= 1
                if prerequisites_count_list[next_course] == 0:
                    course_queue.append(next_course)
                    course_order.append(next_course)

        if count == numCourses:
            return course_order
        else:
            return []
