// import axios from 'axios';

const blocks = document.getElementsByClassName("block-img");
// const main_left = document.getElementsByClassName("main-left");


function handleClick(event){
    const video_id = event.target.id;
    console.log(video_id);
    location.href=`/${video_id}`
};

const block_len = blocks.length

for(var i =0; i<block_len;i++){
    blocks[i].addEventListener("click",handleClick);
}
console.log("YES");
