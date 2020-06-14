let p = document.querySelectorAll('.form > p');
p.map((item,index)=>{
    if(index===2){
        item.className='custom-file'
    }
})