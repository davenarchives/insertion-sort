# insertion-sort
A user-input insertion sort in ascending and descending order

<h1>Insertion Sort</h1>

- **Insertion sort** is a simple sorting algorithm that works similarly to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed in the correct position in the sorted part.

<h2>Insertion Sort Algorithm</h2>

- *To sort an array of size N in ascending order iterate over the array and compare the current element (key) to its predecessor, if the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.*

<h3>How it Works: </h3>

<img align="right" alt="Coding" width="450" src="https://github.com/davenarchives/insertion-sort/assets/160004612/dcf0e975-2d6f-46fc-8a6b-fa3988bf84ee">

  Unsorted Array: [55, -2, 34, 10, 0, 2, -5, 12]
- Start with the first element (55) as sorted
- For each remaining element:
- Compare it with the sorted elements (from right to left)
- If it's smaller, shift larger elements right to make space
- Insert the element in the correct position
- Repeat until all elements are processed.

This will result in the sorted array: [-5, -2, 0, 2, 10, 12, 34, 55]

<h3>Advantages:</h3>

- **Simplicity**: Insertion sort is very easy to understand and implement, making it a good choice for beginners or for scenarios where code readability is important.
- **Efficiency for small lists**: For small datasets, insertion sort can be quite efficient because its processing time grows linearly with the number of elements (in the best case).
- **Partially sorted data**: If the data is already partially sorted, insertion sort can take advantage of that order, leading to faster sorting compared to its average performance.
- **In-place sorting**: Insertion sort sorts the data within the original array, requiring minimal additional memory space.
- **Stable sorting**: Insertion sort preserves the original order of equal elements. This can be useful in specific situations.

<h3>Disadvantages:</h3>

- **Inefficiency for large lists**: Insertion sort's performance deteriorates significantly for large datasets. Its time complexity becomes quadratic (O(n^2)), meaning sorting time increases rapidly with the number of elements.
- **Not as efficient as other algorithms**: There are more efficient sorting algorithms available, such as merge sort or quicksort, which outperform insertion sort for most data sizes.
