//メッセージの表示、編集、削除
if( messages ){
    const div = document.querySelector(".message-box");
    messages.forEach((message) => {
        if(message.uid === uid) {
            const divBox = document.createElement("div");
            const pMessageDate = document.createElement("p");
            const pMessageMsg = document.createElement("p");
            const updateMsgBtn = document.createElement("button");
            const deleteMsgBtn = document.createElement("button");
            const imgBox = document.createElement("div");
        
            pMessageDate.classList.add("message-updatetime-right");
            if(message.created_at === message.updated_at) {
                pMessageDate.innerText = message.created_at;
            } else {
                pMessageDate.innerText = message.created_at+" (編集:"+message.updated_at+")";
            }
            divBox.classList.add("box");
            divBox.classList.add("box-right");
            pMessageMsg.innerText = message.message;
            updateMsgBtn.setAttribute("id","update-message-btn");
            updateMsgBtn.innerText = "編集";
            deleteMsgBtn.setAttribute("id","delete-message-btn");
            deleteMsgBtn.innerText = "削除";
        
            divBox.appendChild(pMessageMsg);
            // リアクション挿入
            if( messages_reaction ) {
                messages_reaction.forEach((message_reaction) => {
                    if(message.id === message_reaction.mid){
                        const reactionImg = document.createElement("img");

                        reactionImg.classList.add("reaction-img");
                        reactionImg.setAttribute("src",`${location.origin}/static/${message_reaction.icon_path}`);

                        imgBox.appendChild(reactionImg);
                    }
                });
            }
            divBox.appendChild(imgBox);
            divBox.appendChild(updateMsgBtn);
            divBox.appendChild(deleteMsgBtn);
            div.appendChild(pMessageDate);
            div.appendChild(divBox);
            
            updateMsgBtn.addEventListener("click", () => {
                modalOpen("update-message");
                const updateMessageIdConfirm = document.getElementById("update-messageid-confirm");
                updateMessageIdConfirm.setAttribute("value", message.id);
            });    
            deleteMsgBtn.addEventListener("click", () => {
                modalOpen("delete-message");
                const deleteMsgConfirmBtnLink = document.getElementById("delete-messageid-confirm");
                deleteMsgConfirmBtnLink.setAttribute("value", message.id);
            });
        }
        else {
            const divBox = document.createElement("div");
            const pUserName = document.createElement("p");
            const pMsgDateExt = document.createElement("p");
            const pMsgExt = document.createElement("p");
            const reactionBtn = document.createElement("button");
            const imgBox = document.createElement("div");
        
            pUserName.classList.add("user-name");
            pUserName.innerText = message.user_name;
            pMsgDateExt.classList.add("message-updatetime-left");
            if(message.created_at === message.updated_at){
                pMsgDateExt.innerText = message.created_at;
            } else {
                pMsgDateExt.innerText = message.created_at+" (編集:"+message.updated_at+")";
            }
            divBox.classList.add("box");
            divBox.classList.add("box-left");
            pMsgExt.innerText = message.message;
            reactionBtn.setAttribute("id","reaction-btn");
            reactionBtn.innerText = "リアクション";
        
            divBox.appendChild(pMsgExt);
            // リアクション挿入
            if( messages_reaction ) {
                messages_reaction.forEach((message_reaction) => {
                    if(message.id === message_reaction.mid){
                        const reactionImg = document.createElement("img");
                        const reactionLink = document.createElement("a");

                        //リアクション挿入した本人なら、削除できる
                        if(uid === message_reaction.uid){
                            reactionLink.setAttribute("href",`/delete_reaction/${channel.id}/${message_reaction.id}`);
                            reactionImg.classList.add("my-reaction-img");
                            reactionImg.setAttribute("src",`${location.origin}/static/${message_reaction.icon_path}`);

                            reactionLink.appendChild(reactionImg);
                            imgBox.appendChild(reactionLink);
                        } else {
                            reactionImg.classList.add("reaction-img");
                            reactionImg.setAttribute("src",`${location.origin}/static/${message_reaction.icon_path}`);

                            imgBox.appendChild(reactionImg);
                        }
                    }
                });
            }
            divBox.appendChild(imgBox);
            divBox.appendChild(reactionBtn);
            div.appendChild(pUserName);
            div.appendChild(pMsgDateExt);
            div.appendChild(divBox);

            reactionBtn.addEventListener("click", () => {
                modalOpen("reaction");
                const reactionConfirmLink = document.getElementsByClassName("reaction-messageid-confirm");
                for(let i=0; i<reactions.length ; i++){
                    reactionConfirmLink[i].setAttribute("value", message.id);
                }
            });
        }
    });
}
