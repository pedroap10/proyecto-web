import React,{useEffect,useState} from "react";
import axios from "axios";
import Swal from "sweetalert2";
import { withReactContent } from "sweetalert2-react-content";
import { show_popup } from "../functions";
 
const ListCars=()=>{
    const url="http://127.0.0.1:5000/cars";
    const [cars,setCars]=useState([]);
    const [id,setId]=useState('');
    const [name,setName]=useState('');
    const [model,setModel]=useState('');
    const [doors,setDoors]=useState('');
 
    useEffect(()=>{
        getCars();
    },[]);
    const getCars=async()=>{
        const dataresponse=await axios.get(url);
        console.log(dataresponse.data.cars)
        setCars(dataresponse.data.cars);
    }
    
    return(
        <div>
        <table>
            <thead>
            <tr>
                <th>#</th>
                <th>Nombre</th>
                <th>Model</th>
                <th>Doors</th>
            </tr>
            </thead>
            <tbody>
                {cars.map((car,index)=>(
                        <tr key={car.index}>
                            <td>{index+1}</td>
                            <td>{car.name}</td>
                            <td>{car.model}</td>
                            <td>{car.doors}</td>
                        </tr>
                ))}
            </tbody>
        </table>
                </div>  
    )
 
    
   //return(<div>Hola</div>)
}
 
export default ListCars;
