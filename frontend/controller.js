import axios from "axios"

let items = [];
let raw_datas=[];
let cur_code="";

const getItems = async()=>{
    await axios.get('http://localhost:5000/video_ids')
      .then(function (response) {
        console.log(response.data.video_id);
        items=response.data.video_id; 
    })
    .catch(function (error) {
        console.log(error);
    });
}


export const home = (req,res)=>{
    // const items=['vPajDFsAxPc', 'ML9E33z2jJ0', 'MwA0qe_JkhI', '6SvFHaG7Aic', 'rsaERcPAKWQ', 'VyxPfzbp61Y', '_ysomCGaZLw', 'qVOMWyHJx98', 'Wmyps0DAbrY', '4_pO7cFrjIU', 'hsWzQGVvZH0', 'XE1IWe_Rzbg', '8rpzKC7gR3w', '7RPGcG-AnCw', 'erqDyYKDEQs', 'm-HStXuBpLw', 'YlkBPvPmhms', 'r7ZZCKmX2OI', 'bb2TevGaKxs', 'NRLnt-UKPwg', 'ZptwLcJOT6g', 'X3biPodSSZc', '5dS7jMKQAaA', 'vLvqWv1y98M', 'QEJYtqfLGvQ', 'liJHNlqoCKQ', 'B8G9RVLIW_4', 'lNiibdMivuk', 'wzP_xFtsTb8', 'n9Py0R5nkiw', 'hkPltLrLT5o', 'rvQgkHgch3g', '2uYLjRGqi0U', 'LGXOb2wCJm0', 'jGLL89RiYOQ', 'pyZMG6DPDPs', 'S1P0dPWAis4', 'aJwyJib1d_I', 'r0pX4Sioszs', 'WBaTWSbcEfQ', 'dvkmUxgMUzA', 'EuHu9BsErRs', 'WxoWRiJNot4', 'XM8n9Njh2Ac', 'aIGSgI0uku8', 'FRmPq7QccKc', '1AWfmN6b0C8', '541EwdsvQZs', 'wHMmN1v-SPg', 'YopSepC9RuA']
    // console.log(items);
    if (items.length === 0){
        getItems()
    }
    console.log("home",cur_code);
    res.render("home",{items,raw_datas})
};

export const code = (req,res)=>{
    // const items=[]
    const {
        params : {
            code: video_id
        }
    }=req
    // console.log(video_id);
    if(video_id !== "favicon.ico"){
      cur_code = video_id;
    }

    axios.post('http://localhost:5000/wordcloud', {
        video_id: video_id,
      })
      .then(function (response) {
        
        if (response.data.length !==0){
          raw_datas=response.data
        }
        console.log(raw_datas);
      })
      .catch(function (error) {
        console.log(error);
      });
    res.redirect("/")
};