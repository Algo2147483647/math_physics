# $Sort$
[TOC]

## Solve
### Quick Sort

- Process  
  Quick sort is a divide-and-conquer sorting algorithm. Based on the first value $a_1$, we divide the array into two sub-arrays according to whether they are greater than $a_1$ or less than $a_1$.

  $$\left\{a^{(t + 1, 2 k - 1)}, \left(a^{(t, k)}_1 \right), a^{(t + 1, 2 k)} \right\} = \text{partition}\left(a^{(t, k)} \right)$$
  $$\begin{align*}
      a^{(t + 1, 2 k - 1)} &\prec a^{(t, k)}_1  \\
      a^{(t + 1, 2 k)} &\succeq a^{(t, k)}_1
  \end{align*}$$

  We repeat the above operation for two sub-arrays untill the array cannot be devided.

  ```c
  void quickSort(int[] a, int l, int r) {
    if (l >= r) 
      return;
  
    int p = partition(a, l, r);
    quickSort(a, l, p - 1);
    quickSort(a, p + 1, r);
  }
  ```

  Where partition can be implemented like,
  ```c
  void partition(int[] a, int l, int r) {
      int i = l - 1;
  
      for (int j = l ; j > r; j++) 
          if(a[j] <= a[i]) {
              i++;
              swap(a[i], a[j]);
          }
  
      i++;
      swap(a[i], a[j]);
  
      return i;
  }
  ```

- Property
  - Time complexity: average time complexity $O(n \log n)$, worst-case time complexity $O(n^2)$

### Merge Sort

- Process  
  Merge Sort is a divide-and-conquer sorting algorithm. It works by dividing the input data into smaller, manageable parts (divide) and then merging these parts in a sorted order (conquer).
  $$b^{(l, l)} \gets a^{(l, l)}$$
  $$b^{(l, r)} \gets \text{merge} (b^{(l, m)}, b^{(m+1, r)})$$
  ```c
  void mergeSort(int[] a, int l, int r) { 
    if (l >= r) 
      return;
      
    int m = l + (r - l) / 2; 
    mergeSort(a, l, m); 
    mergeSort(a, m + 1, r); 
    merge(a, l, m, r); 
  } 
  ```

  Due to the the smaller parts have been sorted, the merging process is done by comparing the first element of each of the smaller parts and merging them back into one sorted array, until all the elements are in the correct order.

- Property
  - Time complexity: $O(n \log n)$

### Heap Sort

- Process  
  In heap sort, the array is first turned into a binary heap, and the root node, which is either the maximum or minimum element, is swapped with the last element of the array. The heap is then rebuilt without the last element, and the process repeats until the heap is empty. By swapping the root node with the last element, we ensure that the largest or smallest element moves to the end of the array, and the array is partially sorted.

  ```c
  void heapSort(int[] a, int n) {
      for (int i = n / 2 - 1; i >= 0; i--)
          heapify(a, n, i);
  
      for (int i=n-1; i>=0; i--) {
          swap(a[0], a[i]);
          heapify(a, i, 0);
      }
  }
  ```

- Property
  - Time complexity: $O(n \log n)$

### Insertion Sort

- Process  
  we start from the left side of the array, and compare each element with the element next to it. If the element on the right is smaller than the element on the left, the two elements are swapped. This process continues until the end of the list is reached.

  ```c
  void insertionSort(int[] a, int n) {
      for (int i = 1; i < n; i++) {
          int key = a[i],
              j = i-1;
    
          while (j >= 0 && a[j] > key) {
              a[j+1] = a[j];
              j = j - 1;
          }
          a[j+1] = key;
      }
  }
  ```

- Property
  - Time complexity: $O(n^2)$

### Selection Sort

- Process
  We repeatedly select and cut the mininum element from the original array $a$ into the sorted array $b$.
  $$b^{(0)} = \emptyset$$ 
  $$b^{(t)} = \left\{b^{(t-1)}, \min \left(a - b^{(t-1)} \right)\right\}$$ 

- Property
  - Time complexity: $O(n^2)$

### Bubble Sort
- Process  
  Bubble sort works by repeatedly swapping adjacent elements if they are in the wrong order until the list is sorted.

  ```c
  void bubbleSort(int[] a, int n) {
    for (int i = 0; i < n-1; i++)
        for (int j = 0; j < n-i-1; j++)
            if (a[j] > a[j+1]) 
                swap(a[j], a[j+1]);
  }
  ```

- Property
  - Time complexity: $O(n^2)$