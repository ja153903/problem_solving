/**
 * Best Time to Buy and Sell Stock
 *
 * This problem wants us to find the lowest buy and highest sell.
 * We can do this with a linear scan of the prices.
 * At each price, we updated the minimum buy and also update the maximum profit we can make
 * @param {number[]} prices
 * @return {number}
 */
function maxProfit(prices) {
  // Base case: if the array is empty, we return 0
  if (!prices || !prices.length) {
    return 0;
  }

  // we set the initial minimum buy to be the first price
  let minBuy = prices[0];

  // we initialize our profit to be 0 since we haven't made a sell yet
  let profit = 0;

  for (let i = 1; i < prices.length; i++) {
    // update the minBuy if we see a lower price
    minBuy = Math.min(minBuy, prices[i]);

    // update the profit by checking to see if we can have an optimal sell
    profit = Math.max(profit, prices[i] - minBuy);
  }

  return profit;
}
