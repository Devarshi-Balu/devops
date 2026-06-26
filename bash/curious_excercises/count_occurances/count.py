import sys, os

def count_the_occurances(string: str, substring: str): 
    return string.split().count(substring)

def main():
    if (len(sys.argv) < 3): 
        error_message = (f"{'*'*50} \n" 
              "hey something is up with the parameters, the right format is \n" 
              "Python count.py 'string' 'substring' \n"
              f"{'*'*50}" 
            )
        raise ValueError(error_message)
        
    string = sys.argv[1]
    substring = sys.argv[2]
    print(count_the_occurances(string, substring))

def main2():
    if (len(sys.argv) < 3): 
        error_message = (f"{'*'*50} \n" 
              "hey something is up with the parameters, the right format is \n" 
              "Python count.py 'filepath' 'substring' \n"
              f"{'*'*50}" 
            )
        raise ValueError(error_message)
    
    with open(sys.argv[1], "r") as f: 
        string = f.read()

    substring = sys.argv[2]
    print(count_the_occurances(string, substring))

def main3():
    from argparse import ArgumentParser
    parser = ArgumentParser(description = "custom script for couting the matching words in a file")

    parser.add_argument("--filepath", "-f", type=str)
    parser.add_argument("--target", "-t", type=str)
    # parser.add_argument("--insensitive", "-i", action="store_true", help="makes case insensitive")
    # action = "store_true", is the flag is set i.e '-i' is written in the command then assign the value true 
    # action = "store_false", same as the above but the false is stored now

    args = parser.parse_args()
    print(args)
    print(vars(args))

    values = {
        key: value # output 
        
        for key, value in vars(args).items() # iteration 
        if value is not None and (len(value) > 1) # filter
    }

    if (len(values) < 2): 
        print("Something is up with arguments")
        sys.exit(1)

    # if an argument is not passed then it is set to None by defualt, 

    """
        args actually looks like this, when you print(args), and len(args) throws an error 
        
        $ python count.py --filepath "./sample.txt" --target "deva"
        Namespace(filepath='./sample.txt', target='deva')

        to convert it into dictionary use vars(args) and now you can use the len function to determine the number of values inside it
    """
    # vars(args) is used to convert the  

    # if (len(vars(args)) < 2): 

    with open(args.filepath, "r") as file: 
        string = file.read()
    
    substring = args.target
    count = string.split().count(substring)
    print(f"The number of occurances of {substring} in {string} is {count}")
        
    
if __name__ == "__main__":
    main3()