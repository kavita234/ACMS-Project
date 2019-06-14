import {LitElement ,html } from 'lit-element';
//import {fs} from 'fs';

class GetAPI extends LitElement{
    static get properties(){
        return {
            userId: Number,
            id:Number,
            title: String,
            completed:Boolean,
            arr : Array,
            data: Array,
        };
    }
    constructor(){
        super();
        this.data=[];
        //this.addEventListener('onchange',this.fileRead);
           }

 fileRead(e)
{
    var fileUpload = this.shadowRoot.getElementById("fileUpload");
    var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.csv|.txt)$/;
    if (regex.test(fileUpload.value.toLowerCase())) {
        if (typeof (FileReader) != "undefined") {
            var reader = new FileReader();
            reader.onload = (e) => {
                var rows = e.target.result.split("\n");
                for (var i = 0; i < rows.length; i++) {
                    var cells = rows[i].split(",");
                    if (cells.length > 1) {
                        for (var j = 0; j < cells.length; j=j+2) {
                            this.fetchData(cells[j],cells[j+1])
                        }
                    }
                }
              // Used inplace of document.getElementbyID    
            }
            reader.readAsText(fileUpload.files[0]);
        } else {
            alert("This browser does not support HTML5.");
        }
    } else {
        alert("Please upload a valid CSV file.");
    }
}
    
fetchData(lon,lat)
{
 console.log(lat,lon);
 const url = "https://api.tomtom.com/search/2/nearbySearch/.json?lat="+lat+"&lon="+lon+"&limit=30&countrySet=IN&idxSet=POI&radius=10000&categorySet=9361,9361067,9361051,7320002,9361063,7315149,7326,7373,7327,9913&key=vDjUYMm75UyPwfH0vRJG9meyxAXgRhjT";
 fetch(url)
 .then(response => response.json())
 .then(json => {
         console.log("Arr "+(this.arr));
         json.results.forEach(element => {
            console.log(element);
             console.log(element.poi.name,element.address.freeformAddress,element.address.municipalitySubdivision,element.poi.categories,element.address.country,element.poi.phone,element.poi.url);
              this.data=[...this.data,[element.poi.name,element.address.freeformAddress,element.address.municipalitySubdivision,element.poi.categories,element.address.country,element.poi.phone,element.poi.url]]
            });
        });
    }
    render(){
        return html `
        <style>
         td{
             text-align: center;
         }
         th{
            width:120pt;
            background-color: green;
              color: white;
              font-weight: 900;
              height:30pt;
         }
         tr:nth-child(even){
              background-color:#DCDCDC;
              height: 30pt;
        }
    
         table{
             margin-top:5px;
             margin-bottom:5px;
            float:left;
            width:100%;
            font-size: 20pt;
         }
          table,td,th{
              border-collapse: collapse;
              border:2px solid black;
              
          }
          input[type="file"]
          {
              width: 60%;
              height: 30pt;
              align-items:center;
              color: Blue;
              border: 2px solid black; 
              border-radius: 5px;
              float:left;
              font-size: 30px;
              padding:0em;

          }
          input[type="button"]
          {
              height: 30pt;
              border-radius: 5px;
              float: left;
              width:37%;

              margin-left: 20pt;
              background-color:#DCDCDC:
              border:2pt solid black;
              font-weight: 900;
              font-size: 20px;

          }
          div{
            background-color: green;
            margin-bottom:5pt;
            height: 50pt; 
            border-radius: 5pt;
          }
          #h1{
            float:left;
            width:100%;
            text-align: center;
            color:white;
            margin-bottom: 5px;
            }
        </style>
        <div id='h1'>
        <h1>Preferable businesses around our cluster centers</h1>
        </div>
        <input type="file" id="fileUpload" value="Choose your data file"/>
        <input type="button" id="upload" value="Upload" @click=${(e)=>{this.fileRead()}} />   
        <div id="disp"></div>
        <table>
        <tr>
        <th>Business name</th>
        <th>Address</th>
        <th>Municipality subdivision</th>
        <th>Business Category</th>
        <th>Country</th>
        <th>Contact No.</th>
        <th>Website</th>
        </tr>     
        ${this.data.map((item,index) => html `<tr> ${this.data[index].map( i => html `<td>${i}</td>` )}</tr>`)}
        </table>
        
        `;
    }
    }
    customElements.define('get-api',GetAPI);