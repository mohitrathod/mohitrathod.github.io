

import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Map.Entry;

/**
 * @author mohit
 * 
 * In a given word find the first un-repeated  letter, e.g., in ‘total’ its ‘o’ and in ‘ teeter’ its ‘r’.
 *
 */
public class FirstUnrepeatedLetter {

	
	public static void main(String[] args) {
		
		firstUnrepeatedLetter("total");
		
		firstUnrepeatedLetter("teeter");
		
	}
	
	
	public static void firstUnrepeatedLetter (String s1) {
		
		String input = s1;
		
		Map<Character, Boolean> charOccouranceMap = new LinkedHashMap<>();
		
		for(Character c : input.toCharArray()) {
			
			if(charOccouranceMap.containsKey(c)) {
				charOccouranceMap.put(c, true);
			}else {
				charOccouranceMap.put(c, false);
			}
			
		}
				
		for (Entry<Character, Boolean> entry : charOccouranceMap.entrySet()) {
			if(entry.getValue()) {
				continue;
			} else {
				System.out.println(entry.getKey());
				break;
			}
		}
		
	}
	
}
