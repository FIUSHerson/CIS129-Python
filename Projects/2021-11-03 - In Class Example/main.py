import os

def write_phil_file(my_file):
    # Open the file
    outfile = open(my_file, 'w')

    # Write to the file
    outfile.write("John Locke\n")
    outfile.write("David Hume\n")
    outfile.write("Edmund Burke\n")

    # Close the file
    outfile.close()


def read_phil_file(my_file):
    infile = open(my_file, 'r')

    lines = infile.read()

    infile.close()

    print(lines)


def main():
    program_dir = os.path.dirname(__file__)
    file_to_use = "files/philosophers.txt"
    final_file = os.path.join(program_dir, file_to_use)
        
    write_phil_file(final_file)
    read_phil_file(final_file)
        

if __name__ == "__main__":
    main()