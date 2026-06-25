filepath=$1
substring=$2

# use -v to set some variable for the awk 
# not specifying anything for -F --> makes any whitespace character or tabs as the seperator  

awk -v target=$substring  \
'   
    BEGIN {
        count = 0
        iteration = 1
    }

    {
        for (i = 1; i<=NF; i++){
            if ($i == target){
                count++
            }
        }

        iteration++
    }

    END{
        print "The total occurances of the word=" target  " is " count
        print "the total number of iterations is: " iteration
    }

' "$filepath"