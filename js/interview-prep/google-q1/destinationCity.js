/**
 * @param {string[][]} paths
 * @return {string}
 */
const destCity = function(paths) {
  const departure = new Set();
  const arrival = new Set();

  for (const [dept, arr] of paths) {
    departure.add(dept);
    arrival.add(arr);
  }

  // look for a city that exists within arrival but not in departure
  for (const city of arrival) {
    if (!departure.has(city)) {
      return city;
    }
  }

  return '';
};