def binary_search(array, target, start, end):
  #종료 조건
  if start > end:
    return None
  
  #중간점 설정
  mid = (start + end) // 2

  #중간값이 찾으려는 값보다 작은 경우
  if array[mid] < target:
    #중간값 기준으로 왼쪽 영역을 탐색
    return binary_search(array, target, start, mid-1)
  #중간값이 찾으려는 값보다 큰 경우
  elif array[mid] > target:
    #중간값 기준으로 오른쪽 영역을 탐색
    return binary_search(array, target, mid+1, end)
  #중간값과 찾으려는 값이 일치할 경우
  else:
    #중간값의 인덱스에 +1한 값을 반환(인덱스는 0부터 시작하므로)
    return mid + 1