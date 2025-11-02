def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(calc_average_temperature(num_list))
    print(calc_min_max_temperature(num_list))
    print(sort_temperature(num_list))
    sorted_list = sort_temperature(num_list)
    print(calc_median_temperature(sorted_list))


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    x = input()
    y = x.split(",") 
    z = []
    for num in y:
        z.append(float(num)) 
    return z

def calc_average_temperature(num_list):
    avg = sum(num_list)/len(num_list)
    return avg

def calc_min_max_temperature(num_list):
    minimum = min(num_list)
    maximum = max(num_list)
    return [minimum,maximum]

def sort_temperature(num_list):
    num_list.sort() 
    sorted_list = num_list
    return sorted_list

def calc_median_temperature(sorted_list):
    n = len(sorted_list)
    mid = n // 2

    if n % 2 == 0: 
       median = (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:  
        median = sorted_list[mid]

    return median

if __name__ == "__main__":
    main()