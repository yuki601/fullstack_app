import axios from "axios";

export default function Page() {
    axios
    .post("/api/inventory/login/")
    .then((response) => {
      console.log(response)
    })
    .catch(function (error){
        console.log(error.response)
    });
}