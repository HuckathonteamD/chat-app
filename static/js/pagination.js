const pagination = () => {
    // 初期設定
    let page = 1; // 今何ページ目にいるか
    const STEP = 8; // ステップ数（1ページに表示する項目数）
    // 全ページ数 channelsリストの総数/ステップ数の余りの有無で場合分け
    // 余りがある場合はページを１つ余分に追加する
    const TOTAL =
      channels.length % STEP == 0
        ? channels.length / STEP
        : Math.floor(channels.length / STEP) + 1;
  
    // <ul class="pagination"></ul> の中身(li)を書き換える
    // channel表示のpageがどれだけあるか表示する
    const paginationUl = document.querySelector(".pagination");
    let pageCount = 0;
    while (pageCount < TOTAL) {
      let li = document.createElement("li");
      li.classList.add("pagination-li");
      if(pageCount == 0) li.classList.add("colored");
      li.setAttribute("id","page"+(pageCount+1));
      li.innerText = pageCount + 1;
      paginationUl.appendChild(li);
      if(pageCount != TOTAL-1){
        const span = document.createElement("span");
        span.innerText = "・";
        paginationUl.appendChild(span);
      }
      pageCount++;
    }

  // <ul class="channel-box"></ul> の中身(li)を書き換える
  // channelを表示させるための関数
  const show = (page, STEP) => {
    const ul = document.querySelector(".channel-box");
    // 一度リストを空にする
    ul.innerHTML = "";

    const first = (page - 1) * STEP + 1;
    const last = page * STEP;
    channels.forEach((item, i) => {
      if (i < first - 1 || i > last - 1) return;
      const a = document.createElement("a");
      const li = document.createElement("li");
      const p = document.createElement("p");
      const div = document.createElement("div");
      const followBtn = document.createElement("button");
      const followImg = document.createElement("img");
      const unfollowImg = document.createElement("img");

      // const br =document.createElement("br");

      // チャット画面へのリンク追加
      const url = `/detail/${item.id}`;
      a.setAttribute("href", url);

      li.classList.add("channel-list");
      div.classList.add("channel-item");
      a.classList.add("channel-name");
      a.innerText = item.name;
      div.appendChild(a);
      p.innerText = item.abstract;
      p.classList.add("channel-abstract");
      div.appendChild(p);
      li.appendChild(div);

      var follow_judge = 0;

      // フォローしているチャンネルがない場合、フォローボタンを表示
      if (follow_channels[0] == null) {
        const followChannelBtn = document.createElement("button");
          followChannelBtn.classList.add("follow-channel-btn-i")
          followImg.setAttribute("src",`${location.origin}/static/img/channelPic-heartLine.png`);
          followChannelBtn.appendChild(followImg);
          li.appendChild(followChannelBtn);

          followChannelBtn.addEventListener("click", () => {
            modalOpen("follow_i");
            const confirmationButtonLink = document.getElementById(
              "follow-confirm-link-i"
            );
            const url = `/follow_channel_i/${item.id}`;
            confirmationButtonLink.setAttribute("href", url);
          });
      } else {
        for (let i=0; i < follow_channels.length; i++){
          if (item.id === follow_channels[i].cid) {
            follow_judge += 1;
          } else {
            follow_judge += 0;
          }
        }
        // フォローしているチャンネルには、フォロー解除ボタンを表示
        if (follow_judge === 1) {
          const unfollowChannelBtn = document.createElement("button");
          unfollowChannelBtn.classList.add("unfollow-channel-btn-i")
          unfollowImg.setAttribute("src",`${location.origin}/static/img/channelPic-heart.png`);
          unfollowChannelBtn.appendChild(unfollowImg);
          li.appendChild(unfollowChannelBtn);

          unfollowChannelBtn.addEventListener("click", () => {
            modalOpen("unfollow_i");
            const confirmationButtonLink = document.getElementById(
              "unfollow-channel-confirm-link-i"
            );
            const url = `/unfollow_channel_i/${item.id}`;
            confirmationButtonLink.setAttribute("href", url);
          });
        } else {
          // フォローしていないチャンネルには、フォローボタンを表示
          const followChannelBtn = document.createElement("button");
          followChannelBtn.classList.add("follow-channel-btn-i")
          followImg.setAttribute("src",`${location.origin}/static/img/channelPic-heartLine.png`);
          followChannelBtn.appendChild(followImg);
          li.appendChild(followChannelBtn);

          followChannelBtn.addEventListener("click", () => {
            modalOpen("follow_i");
            const confirmationButtonLink = document.getElementById(
              "follow-confirm-link-i"
            );
            const url = `/follow_channel_i/${item.id}`;
            confirmationButtonLink.setAttribute("href", url);
          });
        }
      }


      // もしチャンネル作成者uidとuidが同じだったら、削除ボタンを追加
      if (uid === item.uid) {
        const deleteButton = document.createElement("button");
        const deleteimg = document.createElement("img");
        // deleteButton.innerText = "削除";
        deleteButton.classList.add("delete-channel-btn");
        deleteimg.setAttribute("src",`${location.origin}/static/img/trashIcon.png`);
        deleteButton.appendChild(deleteimg);
        li.appendChild(deleteButton);
        deleteButton.addEventListener("click", () => {
          modalOpen("delete");
          const confirmationButtonLink = document.getElementById(
            "delete-confirm-link"
          ); // aタグ
          const url = `/delete/${item.id}`;
          confirmationButtonLink.setAttribute("href", url);
        });
      }
      ul.appendChild(li);
      // ul.appendChild(br);
    });
  };

  // pagination内で現在選択されているページの番号に色を付ける
  const colorPaginationNum = () => {
    // <ul class="pagination"></ul>内の<li></li>を全て取得し、配列に入れる
    // ループさせて一度全ての<li></li>から　class="colored"を削除
    const paginationArr = [...document.querySelectorAll(".pagination li")];
    paginationArr.forEach((page) => {
      page.classList.remove("colored");
    });
    // 選択されているページに　class="colored"を追加（背景色が変わる）
    paginationArr[page - 1].classList.add("colored");
  };

  // 最初に1ページ目を表示
  show(page, STEP);


  // 前ページ遷移
  document.getElementById("prev").addEventListener("click", () => {
    if (page <= 1) return;
    page = page - 1;
    show(page, STEP);
    colorPaginationNum();
  });



  // 次ページ遷移
  document.getElementById("next").addEventListener("click", () => {
    if (page >= channels.length / STEP) return;
    page = page + 1;
    show(page, STEP);
    colorPaginationNum();
  });

  for(let j=1;j<=TOTAL;j++){
    document.getElementById(`page${j}`).addEventListener("click", () => {
      page = j;
      show(page, STEP);
      colorPaginationNum();
    });
  }
}

window.onload = () => {
  pagination();
};
