var data = [ {

		z: [],

		x: [],

		y: [],

		type: 'contour'

	}

];


async function fetchsim(k,q,L,Ttop,Tbtm,Tleft,Tright) {
    try {
        const response = await fetch('/calculate?' + new URLSearchParams({
            k: k,
            q: q,
            L: L,
            Ttop: Ttop,
            Tbtm: Tbtm,
            Tleft: Tleft,
            Tright: Tright
        }).toString())
        if (!response.ok) {
            throw new Error('Response status :$(response.status)')
        }
        const data  = await response.json()
        return data
    }
    catch (error) {
        console.error(error)
    }    
}

fetchsim(1,1,1,0,0,0,0).then(value => {
    data[0].x = value.x
    data[0].y = value.y
    data[0].z = value.T
    Plotly.newPlot('plot', data);
})

function calculate() {
    console.log("Calulating...")
    var Ttop = document.querySelector("#Ttop").value
    var Tbottom = document.querySelector("#Tbottom").value
    var Tleft = document.querySelector("#Tleft").value
    var Tright = document.querySelector("#Tright").value
    var k = document.querySelector("#k").value
    var q = document.querySelector("#q").value
    var L = document.querySelector("#L").value
    fetchsim(k,q,L,Ttop,Tbottom,Tleft,Tright).then(value => {
        data[0].x = value.x
        data[0].y = value.y
        data[0].z = value.T
        Plotly.newPlot('plot', data);
})}