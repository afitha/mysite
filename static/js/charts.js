function getproddata(){
    var xhttp= new XMLHttpRequest()
        xhttp.open('GET','/home/getpro/'+document.getElementById('keyword').value,true)
        xhttp.onreadystatechange=function(){
            if(this.readyState==4 & this.status==200){
                var data=JSON.parse(this.responseText)
                str='<table>'
                for(x of data.produ){
                    str=str+'<tr>'
                    str=str+'<td>'+(x.id)+'<td>'
                    str=str+'<td>'+(x.name)+'<td>'
                    str=str+'<td>'+(x.price)+'<td>'

                }
                str=str+'</table>'
                document.getElementById('data').innerHTML=str
                
            }
        };
        xhttp.send();
    }


function drawdata(){
    var xhttp= new XMLHttpRequest()
        xhttp.open('GET','/home/jsondata',true)
        xhttp.onreadystatechange=function(){
            if(this.readyState==4 & this.status==200){
                var datax=JSON.parse(this.responseText)
                thechart(datax)
                
            }
        };
        xhttp.send();
}

function thechart(datax){
    const myChart = new Chart(document.getElementById('myChart'),
    {
        type: 'line',
        data: {
                labels:getlabeldata(datax) ,
                datasets: [{
                    label: 'My first dataset',
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(255, 99, 132)',
                    data:getdata(datax),
                }]
            },
            options: {}
            });    
}
function getlabeldata(datax){
    let labels=[]
    for(x of datax.new){
        labels.push(x.name)
    }
    return labels
}
function getdata(datax){
    let labels=[]
    for(x of datax.new){
        labels.push(x.price)
    }
    return labels
}
 