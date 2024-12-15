array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def selectionSort(array):
  for i in range(len(array)):
    min_index = i #탐색 범위에서 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
      if array[min_index] > array[j]:
        min_index = j
    array[i], array[min_index] = array[min_index], array[i] #작은 원소를 i번째와 swap

selectionSort(array)
print(array)