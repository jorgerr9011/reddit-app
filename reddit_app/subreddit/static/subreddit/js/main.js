const getOptionChart = async()=>{
    try {
        const response=await fetch("http://localhost:8001/subreddit/chart/");
        return await response.json();
    } catch (ex){
        alert(ex);
    }
};

const initChart = async() => {
    const myChart=echarts.init(document.getElementById("chart"));

    myChart.setOption(await getOptionChart());

    myChart.resize();
};

window.addEventListener("load", async() => {
    await initChart();
});

