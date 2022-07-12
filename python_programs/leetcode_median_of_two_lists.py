
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
sorted_list=sorted(nums1+nums2)
mid=len(sorted_list)//2
print(f'{ (sorted_list[mid]+sorted_list[~mid])/2 :.5f}')
