from flask import request, Blueprint, render_template, url_for, session, jsonify

# from . import openAI_client
from .summarizer import Summarizer

views = Blueprint("views", __name__)


@views.route('/get-summary', methods=['POST'])
def get_summary():

    data = request.json
    url = data.get('url')
    start_time = Summarizer.timestamp_to_seconds(int(data.get('startTime')))
    end_time = Summarizer.timestamp_to_seconds(int(data.get('endTime')))
    word_count = int(data.get('wordCount'))

    summary = Summarizer.getFinalsummary(url, word_count, start_time, end_time)

    # title = Summarizer.get_title(youtube_url)
    # url = Summarizer.get_url(youtube_url)
    # summary = Summarizer.get_summary(youtube_url, word_count, start_time, end_time)
    title = "this is the title"

    # summary = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ab quo architecto, id nam ratione dicta obcaecati ad maxime saepe laboriosam doloremque. Numquam consectetur itaque sit. Tempore odio enim at iusto eveniet! Esse ipsa quo rerum blanditiis ipsum impedit quaerat unde alias voluptas ex quos nostrum eos magni sunt facere beatae odit provident maiores nulla, fugiat vel eveniet velit et. Hic accusantium debitis numquam consequatur quod voluptatum ab illo earum reiciendis alias aliquid eos excepturi optio et, repellendus id facilis vitae nobis cum voluptates exercitationem culpa possimus iure. Tenetur odio consequuntur eum provident veritatis, modi iste eligendi deserunt, sequi nihil excepturi alias, laboriosam ea. Exercitationem, ipsa. Veritatis, eius voluptatem. Atque mollitia impedit accusamus nostrum eaque cupiditate hic pariatur sequi! Suscipit tempore veritatis quae illo eos sequi unde quam nesciunt quaerat labore, aliquid reprehenderit, doloribus incidunt vel totam explicabo placeat! Et impedit libero, quam vero, quis id dolorem similique, culpa laboriosam cumque nemo accusantium odio corporis qui placeat labore? Nesciunt dolore dolorum quae alias voluptatum maiores iste dolor natus illo? Aliquid, repudiandae esse. Molestias harum tempora, dignissimos repellat aut at distinctio minima? Mollitia tempore quam architecto ut tenetur atque dolorem deleniti velit, perspiciatis asperiores delectus aliquam? Sapiente repellendus pariatur, temporibus eveniet illum rerum alias quis aliquam nobis quam vel, adipisci provident reprehenderit repudiandae aperiam eius voluptas quo dolorem maiores. Iusto veniam sunt accusamus unde impedit consectetur tenetur, ipsum quibusdam? Fugiat porro quaerat commodi sequi nihil at, harum deleniti perferendis esse a. Ipsam esse commodi, error laboriosam quaerat porro nesciunt, numquam molestiae sit fuga rerum consectetur voluptas iste voluptate. Veritatis animi minus nihil quas nulla laudantium autem perspiciatis, fugiat repudiandae obcaecati quod culpa dolore aut debitis officia possimus nobis nostrum iste, ad perferendis tenetur! Distinctio beatae architecto, est illum soluta, doloremque minima nulla fugit ducimus aliquid sapiente delectus veniam adipisci aperiam inventore esse nesciunt officia unde a eos ab non. Asperiores omnis, laudantium nihil blanditiis illum expedita similique nesciunt harum quae ipsum nobis repellendus cum quia nemo, ipsa, deleniti exercitationem ratione in perspiciatis nostrum? Quidem maiores nulla recusandae eligendi consectetur amet qui quae, assumenda explicabo officia tempora suscipit. Quidem deserunt temporibus sequi facilis a, rerum odit ipsa? Cum ex porro, praesentium, mollitia eligendi doloremque facilis doloribus autem neque, tempore sequi? Aperiam non ratione excepturi consequuntur, ullam nisi expedita mollitia repellendus totam deleniti ut officiis perspiciatis eius dicta facilis magnam esse sit quasi, fuga omnis aliquam libero, eveniet commodi. Laboriosam recusandae amet est quidem facilis vel numquam sint temporibus? Aliquid non magnam maiores quia provident expedita ut mollitia, ad ducimus laboriosam sit ea assumenda iure soluta. Alias animi consectetur praesentium nemo eveniet perferendis earum distinctio a ex totam? Quaerat repudiandae exercitationem quam voluptates quos repellendus sint ipsa, laborum explicabo, earum architecto, eveniet fugiat maiores? Assumenda incidunt, ut eligendi earum suscipit aspernatur obcaecati rem sapiente esse molestiae consequatur neque facilis excepturi odit iste officia architecto accusantium et fugit magnam in. Dicta atque voluptate, dolorem dolores vitae pariatur sint ipsam quasi nulla excepturi. Delectus sit fuga quia, sint, consequuntur hic vel veritatis culpa ullam, quo voluptas."

    if not url:
        return jsonify({"error": "No URL provided"})

    return jsonify({"video_title": title, "video_url": url, "summary": summary})
