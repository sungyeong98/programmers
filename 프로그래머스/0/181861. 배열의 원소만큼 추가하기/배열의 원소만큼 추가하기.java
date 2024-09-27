import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.Collectors;
class Solution {
    public int[] solution(int[] arr) {
        return Arrays.stream(arr)
                    .flatMap(a->IntStream.range(0,a)
                    .map(i->a)).boxed()
                    .collect(Collectors.toList())
                    .stream()
                    .mapToInt(Integer::intValue)
                    .toArray();
    }
}