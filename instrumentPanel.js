var instrumentPanel = {id:"instrumentPanel" , cols:[
            {view: "template", id:"speed", template: "<canvas id='speed'></canvas>"},
            {view: "template", id:"revs", template: "<canvas id='revs'></canvas>"},
            {view: "template", id:"temp", template: "<canvas id='temp'></canvas>"}
            ]
    };    

var tempGaugeDef =  {renderTo: 'temp',
width: 300,
height: 300,
units: "°C",
title: "Temperature",
minValue: -50,
maxValue: 50,
majorTicks: [
    -50,
    -40,
    -30,
    -20,
    -10,
    0,
    10,
    20,
    30,
    40,
    50
],
minorTicks: 2,
strokeTicks: true,
highlights: [
    {
        "from": -50,
        "to": 0,
        "color": "rgba(0,0, 255, .3)"
    },
    {
        "from": 0,
        "to": 50,
        "color": "rgba(255, 0, 0, .3)"
    }
],
ticksAngle: 225,
startAngle: 67.5,
colorMajorTicks: "#ddd",
colorMinorTicks: "#ddd",
colorTitle: "#eee",
colorUnits: "#ccc",
colorNumbers: "#eee",
colorPlate: "#222",
borderShadowWidth: 0,
borders: true,
needleType: "arrow",
needleWidth: 2,
needleCircleSize: 7,
needleCircleOuter: true,
needleCircleInner: false,
animationDuration: 1500,
animationRule: "linear",
colorBorderOuter: "#333",
colorBorderOuterEnd: "#111",
colorBorderMiddle: "#222",
colorBorderMiddleEnd: "#111",
colorBorderInner: "#111",
colorBorderInnerEnd: "#333",
colorNeedleShadowDown: "#333",
colorNeedleCircleOuter: "#333",
colorNeedleCircleOuterEnd: "#111",
colorNeedleCircleInner: "#111",
colorNeedleCircleInnerEnd: "#222",
valueBoxBorderRadius: 0,
colorValueBoxRect: "#222",
colorValueBoxRectEnd: "#333"
};