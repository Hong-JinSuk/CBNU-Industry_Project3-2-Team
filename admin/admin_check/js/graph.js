var series = ["user1", "user2","user3"];
 
var dataset = [ 
    {'월':116, '화':159, '수':134, '목':27, '금':55, '토':24,  '일':45},
    {'월':17, '화':27, '수':37, '목':27, '금':17, '토':7,  '일':9}];

var keys = d3.keys(dataset[0]);
var data = [];

dataset.forEach(function(d, i) {
data[i] = keys.map(function(key) { return {x: key, y: d[key]}; })
});
