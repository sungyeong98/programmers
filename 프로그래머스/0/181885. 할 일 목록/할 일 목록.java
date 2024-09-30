import java.util.*;
import java.util.stream.IntStream;
class Solution {
    public String[] solution(String[] todo_list, boolean[] finished) {
        return IntStream.range(0,todo_list.length).filter(x->!finished[x]).mapToObj(x->todo_list[x]).toArray(String[]::new);
    }
}