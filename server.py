from flask import Flask, request, jsonify
import util
import sys

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return """
		<!DOCTYPE html>
<html>
   <head>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400&display=swap" rel="stylesheet">
   </head>
   <body style="background: #eee; margin: 0; padding: 0">
      <div style="margin-left: 10%; background: #fff; width: 80%; border-radius: 12px; max-height: 100%">
         <h1 style="font-family: 'Poppins', sans-serif; text-align: center; padding: 1rem;">
         <img src="https://github.com/zuhairabs/housing-framework7/raw/main/img/favicon512.png" width="10%">&nbsp;
         Housing API
         <h1>
         <a onMouseOut="this.style.background='#dadada';this.style.color='#121212'" onMouseOver="this.style.background='crimson';this.style.color='#fafafa'" href="https://github.com/zuhairabs/housing-api/tree/main/model" target="_blank" style="font-size: 16px; border-radius: 10px; font-family: Poppins; text-decoration: none; color: #121212; background: #dadada; padding: 10px; margin: 1rem; display: flex; justify-content: center;">Predicting Models &nbsp;<img width="20px" src="https://cdn2.iconfinder.com/data/icons/pittogrammi/142/95-512.png"></a>
         <h3 style="font-family: 'Poppins', sans-serif; margin-left: 1rem; padding: 1rem;">Get Location Names: </h3>
         <p style="overflow-x: scroll; font-size: 15px; color: rgb(171, 178, 191); background: #121212; font-family: 'Poppins', sans-serif; padding: 1rem; margin: 1rem; border-radius: 10px">
            //javascript implementation
            <br>
            Url: <a style="color: crimson" href="https://apihousing.herokuapp.com/get_location_names">https://apihousing.herokuapp.com/get_location_names</a><br><br>
            <span style="color:rgb(224, 108, 117);">fetch</span>('<span style="color:rgb(152, 195, 121);">https://apihousing.herokuapp.com/get_location_names</span>')
            .<span style="color:rgb(86, 182, 194);">then</span>(<span style="color:rgb(229, 192, 123);">response</span> => <span style="color:rgb(224, 108, 117);">response</span>.<span style="color:rgb(86, 182, 194);">json</span>())
            .<span style="color:rgb(86, 182, 194);">then</span>(<span style="color:rgb(229, 192, 123);">data</span> => <span style="color:rgb(224, 108, 117);">console</span>.<span style="color:rgb(86, 182, 194);">log</span>(<span style="color:rgb(224, 108, 117);">data</span>));
         </p>
         <h3 style="font-family: 'Poppins', sans-serif; margin-left: 1rem; padding: 1rem;">Response: </h3>
         <p style="overflow-x: scroll; font-size: 15px; color: rgb(152, 195, 121); background: #121212; font-family: 'Poppins', sans-serif; padding: 1rem; margin: 1rem; border-radius: 10px">
            {"locations":["1st block jayanagar","1st phase jp nagar","2nd phase judicial layout","2nd stage nagarbhavi","5th block hbr layout","5th phase jp nagar","6th phase jp nagar","7th phase jp nagar","8th phase jp nagar","9th phase jp nagar","aecs layout","abbigere","akshaya nagar","ambalipura","ambedkar nagar","amruthahalli","anandapura","ananth nagar","anekal","anjanapura","ardendale","arekere","attibele","beml layout","btm 2nd stage","btm layout","babusapalaya","badavala nagar","balagere","banashankari","banashankari stage ii","banashankari stage iii","banashankari stage v","banashankari stage vi","banaswadi","banjara layout","bannerghatta","bannerghatta road","basavangudi","basaveshwara nagar","battarahalli","begur","begur road","bellandur","benson town","bharathi nagar","bhoganhalli","billekahalli","binny pete","bisuvanahalli","bommanahalli","bommasandra","bommasandra industrial area","bommenahalli","brookefield","budigere","cv raman nagar","chamrajpet","chandapura","channasandra","chikka tirupathi","chikkabanavar","chikkalasandra","choodasandra","cooke town","cox town","cunningham road","dasanapura","dasarahalli","devanahalli","devarachikkanahalli","dodda nekkundi","doddaballapur","doddakallasandra","doddathoguru","domlur","dommasandra","epip zone","electronic city","electronic city phase ii","electronics city phase 1","frazer town","gm palaya","garudachar palya","giri nagar","gollarapalya hosahalli","gottigere","green glen layout","gubbalala","gunjur","hal 2nd stage","hbr layout","hrbr layout","hsr layout","haralur road","harlur","hebbal","hebbal kempapura","hegde nagar","hennur","hennur road","hoodi","horamavu agara","horamavu banaswadi","hormavu","hosa road","hosakerehalli","hoskote","hosur road","hulimavu","isro layout","itpl","iblur village","indira nagar","jp nagar","jakkur","jalahalli","jalahalli east","jigani","judicial layout","kr puram","kadubeesanahalli","kadugodi","kaggadasapura","kaggalipura","kaikondrahalli","kalena agrahara","kalyan nagar","kambipura","kammanahalli","kammasandra","kanakapura","kanakpura road","kannamangala","karuna nagar","kasavanhalli","kasturi nagar","kathriguppe","kaval byrasandra","kenchenahalli","kengeri","kengeri satellite town","kereguddadahalli","kodichikkanahalli","kodigehaali","kodigehalli","kodihalli","kogilu","konanakunte","koramangala","kothannur","kothanur","kudlu","kudlu gate","kumaraswami layout","kundalahalli","lb shastri nagar","laggere","lakshminarayana pura","lingadheeranahalli","magadi road","mahadevpura","mahalakshmi layout","mallasandra","malleshpalya","malleshwaram","marathahalli","margondanahalli","marsur","mico layout","munnekollal","murugeshpalya","mysore road","ngr layout","nri layout","nagarbhavi","nagasandra","nagavara","nagavarapalya","narayanapura","neeladri nagar","nehru nagar","ombr layout","old airport road","old madras road","padmanabhanagar","pai layout","panathur","parappana agrahara","pattandur agrahara","poorna pragna layout","prithvi layout","r.t. nagar","rachenahalli","raja rajeshwari nagar","rajaji nagar","rajiv nagar","ramagondanahalli","ramamurthy nagar","rayasandra","sahakara nagar","sanjay nagar","sarakki nagar","sarjapur","sarjapur  road","sarjapura - attibele road","sector 2 hsr layout","sector 7 hsr layout","seegehalli","shampura","shivaji nagar","singasandra","somasundara palya","sompura","sonnenahalli","subramanyapura","sultan palaya","tc palaya","talaghattapura","thanisandra","thigalarapalya","thubarahalli","tindlu","tumkur road","ulsoor","uttarahalli","varthur","varthur road","vasanthapura","vidyaranyapura","vijayanagar","vishveshwarya layout","vishwapriya layout","vittasandra","whitefield","yelachenahalli","yelahanka","yelahanka new town","yelenahalli","yeshwanthpur"]}
         </p>
         
         
         
         <h3 style="font-family: 'Poppins', sans-serif; margin-left: 1rem; padding: 1rem;">Predict House Prices: </h3>
         <p style="font-size: 15px; color: rgb(171, 178, 191); background: #121212; font-family: 'Poppins', sans-serif; padding: 1rem; margin: 1rem; border-radius: 10px">
         <a href="https://ibb.co/CzW2Zvs"><img src="https://i.ibb.co/pxny8Zr/carbon.png" width="100%" height="100%" alt="carbon" border="0"></a>
         </p>
         
         <h3 style="font-family: 'Poppins', sans-serif; margin-left: 1rem; padding: 1rem;">Response: </h3>
         <p style="overflow-x: scroll; font-size: 15px; color: rgb(152, 195, 121); background: #121212; font-family: 'Poppins', sans-serif; padding: 1rem; margin: 1rem; border-radius: 10px;">
            {
    "estimated_price": 81.42
    }
         </p><br>
      </div>
      <br><br>
      <center style="font-family: 'Poppins', sans-serif; margin-left: 1rem; padding: 1rem;">Made By <a style="color: crimson;" href="https://zuhairabs.github.io/">Zuhair Abbas</a><center>
   </body>
</html>
	"""

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(util.get_location_names())
    sys.stdout.flush()

    return response
 
@app.route('/get_data_columns', methods=['GET'])
def get_data_columns():
    response = jsonify({
        'locations': util.get_data_columns()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(util.get_data_columns())
    sys.stdout.flush()

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    sys.stdout.flush()
    app.run()