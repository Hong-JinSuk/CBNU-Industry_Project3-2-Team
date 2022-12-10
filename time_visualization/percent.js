const chart1 = document.querySelector('.doughnut1');

const makeChart = (percent, classname, color) => {
  let i = 1;
  let chartFn = setInterval(function() {
    if (i <= percent) {
      colorFn(i, classname, color);
      i++;
    } else {
      clearInterval(chartFn);
    }
  }, 10);
}

const colorFn = (i, classname, color) => {
  classname.style.background = "conic-gradient(" + color + " 0% " + i + "%, #dedede " + i + "% 100%)";
}

makeChart(75, chart1, '#f5b914');
