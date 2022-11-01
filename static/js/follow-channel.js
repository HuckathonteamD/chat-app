// フォローチャンネルの表示
// <ul class="follow-box"></ul> の中身(li)を書き換える

let followbool = 'true';
const ul = document.querySelector(".follow-box");
ul.innerHTML = "";

console.log(follows);
follows.forEach((item) => {
  if(channel.id === item.cid){
    const li = document.createElement("li");
    li.innerText = "フォロー中です";
    ul.appendChild(li);
    followbool = 'false';
  }
})

if(followbool === 'true'){
  const followButton = document.createElement("button");
  followButton.setAttribute("id","follow-channel-btn");
  followButton.innerText = "フォロー";
  ul.appendChild(followButton);
}
