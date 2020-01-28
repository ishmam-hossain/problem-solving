"""
Using the JavaScript language, have the function DistinctList(arr)
take the array of numbers stored in arr and determine the total number
of duplicate entries. For example if the input is [1, 2, 2, 2, 3]
then your program should output 2 because there are two duplicates of one of the elements.
"""


"""
function DistinctList(arr){
  duplicateCount = 0;

  for(i=1;i<arr.length;i++){
    if(arr[i] === arr[i - 1]){
      duplicateCount ++;
    }
  }
  return duplicateCount;
}


console.log(DistinctList([1, 2, 3, 3, 3, 4, 5, 5, 5, 6]))

"""

"""
function primeTime(n){
  if(n < 2){
    return false
  }
  for(i=2;i<=Math.sqrt(n);i++){
    if(n % i == 0){
      return false;
    }
  }
  return true
}

l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

for(i=0;i<l.length;i++){
  console.log(primeTime(l[i]));
}
"""


"""


"""