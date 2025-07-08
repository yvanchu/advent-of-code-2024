from collections import defaultdict

def get_input():
    with open('./day1.txt', 'r') as file:
        return file.read().strip()

def parse_input(text):
    list1 = []
    list2 = [] 
    for row in text.split('\n'):
        # split on whitespace
        parts = row.split()
        if len(parts) == 2:
            list1.append(int(parts[0]))
            list2.append(int(parts[1]))
        else:
            print(f"Skipping malformed row: {row}")
    return list1, list2

def main():
    text = get_input()
    list1, list2 = parse_input(text)
    
    # part 1: get sorted differences
    list1.sort()
    list2.sort()
    
    diff_sum = sum(abs(a-b) for a, b in zip(list1, list2))
    print(f"Sum of sorted differences: {diff_sum}")
    
    # part 2: get similarity score
    list2_dict = defaultdict(int)
    for num in list2:
        list2_dict[num] += 1
    
    similarity_score = sum(num * list2_dict[num] for num in list1 if num in list2_dict)
    print(f"Similarity score: {similarity_score}")

if __name__ == "__main__":
    main()

