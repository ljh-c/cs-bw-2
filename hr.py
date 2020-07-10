def threeNumberTwoPointer(arr, target):
    triplets = []

    # Sort array
    arr.sort()

    # Loop through nums
    for i, num in enumerate(arr):
        # From current num, do two sum with rest of nums
        sub_t = target - num

        # Low and high pointers to find two sum
        low_i = i + 1   # after current num
        high_i = len(arr) - 1

        while low_i < high_i:
            two_sum = arr[low_i] + arr[high_i]

            if two_sum == sub_t:
                triplets.append([num, arr[low_i], arr[high_i]])
                # Move pointers to find other solutions
                low_i += 1
                high_i -= 1
            elif two_sum < sub_t:
                low_i += 1
            elif two_sum > sub_t:
                high_i -= 1

    return triplets

def threeNumberSum(arr, target):
    triplets = []

    # Sort array
    arr.sort()

    # Dict of num: index
    seen = dict()
    for i, num in enumerate(arr):
        seen[num] = i

    # Loop through nums
    for i, num in enumerate(arr):
        # From current num, do two sum with rest of nums
        sub_t = target - num

        for n in arr[i + 1:]:
            partner = sub_t - n
            
            if partner > n and partner in seen:
                triplets.append([num, n, partner])

    return triplets


def balancedBrackets(string):
    brackets = {'[': ']', '(': ')', '{': '}', '|': '|'}
    closing = {']', ')', '}', '|'}
    # Use stack to keep track of closing bracket
    stack = []

    # Loop through str, one char at a time
    for c in string:
        # Peek at top of stack
        if stack and c == stack[-1]:
            stack.pop()
        elif c in brackets:
            stack.append(brackets[c])
        elif c in closing:
            return False
    
    return not len(stack)


def removeKthLinkedListNode(head, k):
    # Access tail
    curr = head
    size = 1 if head else 0
    
    while curr and curr.next:
        size += 1
        curr = curr.next

    # Access Kth node by re-traversing 
    if k > size:
        return head
    
    prev = None
    curr = head
    hops_to_target = size - k

    # If removing head
    if hops_to_target == 0:
        curr = curr.next
        head.next = None
        
        return curr
    else:
        for i in range(hops_to_target):
            prev = curr
            curr = curr.next
    
        # Reassign pointers
        prev.next = curr.next

    return head

print(balancedBrackets('|{{[s(({}||))]}}|'))