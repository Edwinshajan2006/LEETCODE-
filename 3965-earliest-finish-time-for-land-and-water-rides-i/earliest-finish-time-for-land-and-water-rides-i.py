class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):

        ans = float('inf')

        # Land -> Water
        for i in range(len(landStartTime)):
            land_finish = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                water_start = max(land_finish, waterStartTime[j])
                finish = water_start + waterDuration[j]

                ans = min(ans, finish)

        # Water -> Land
        for j in range(len(waterStartTime)):
            water_finish = waterStartTime[j] + waterDuration[j]

            for i in range(len(landStartTime)):
                land_start = max(water_finish, landStartTime[i])
                finish = land_start + landDuration[i]

                ans = min(ans, finish)

        return ans