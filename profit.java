class Solution {
    public int countHighlyProfitableMonths(int[] stockPrices, int k) {
        int count = 0;
        for(int i = 0; i < stockPrices.length - k + 1; i++) {
            if(Arrays.equals(Arrays.copyOfRange(stockPrices, i, i + k), Arrays.stream(stockPrices, i, i + k).sorted().toArray())) {
                count++;
            }
        }
        return count;
    }
}
