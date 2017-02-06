/*
    Your plant regularly receive environment informations from its next generation captors.
    With this informations you have to choose between 5 actions :
        - grow
            this action takes "stemName" and the direction you want this stem to take.
            if your plant has enough light, nutrient and water it will consume some to grow toward the light.
        - fork
            this action takes "stemName" to fork and "firstChildName" and "secondChildName" to name the two forked stems.
            Of course it consumes nutrient and water. Light position will influence the direction of the two new stems.
        - bloom
            this action consumes a lot of nutrient and takes only "stemName" to bloom as parameter.
        - ted
            same as bloom but to ted the flower (if you want to fork the stem or grow it again for example)
        - restart
            reset your plant.

    you should return result of this form {verb: 'bloom', args: {'stemName': 'magic stem'}}

    To help your plant to choose an action you got three objects :
        - life
            It contains information relative to your plant life
                - nutrient
                - water
            Each action consume some of this life parameters but they also increases with environment (light and temperature) and time.
        - environment
            It contains information about the environment
                - light
                - temperature
                - water
                - lightPosition
        - plant
            plant object represent your plant in an ascii art way.
            It's an array of stem.
            Each stem has a name, a form and an array of children name.
            {"plant":
                [{"name":"stem",
                    "form":"|/\\\\=",
                    "children":["one","two"]
                },{"name":"one",
                    "form":"||||/\\",
                    "children":[]
                },{"name":"two",
                    "form":"/",
                    "children":[]
                }]
            }

    Here is a default script to help you understand the process.
*/


var result = {verb: '', args: {}};

if(plant.length === 1 && plant[0].form.length >5 && environment['light'] > 3 && life['nutrient'] > 6 && life['water'] > 2){
    result.verb = 'grow';
    result.args = {'stemName': 'stem', 'direction': 'top'}
}

if(plant.length > 1 && plant[1].form.length < 6 && environment['light'] > 3 && life['nutrient'] > 6 && life['water'] > 2){
    result.verb = 'grow';
    result.args = {'stemName': 'one', 'direction': 'top'}
}

if(plant.length === 1 && plant[0].form.length > 3 && environment['light'] > 3 && life['nutrient'] > 10 && life['water'] > 4){
    result.verb = 'fork';
    result.args = {'stemName': 'stem', 'firstChildName': 'one', 'secondChildName': 'two'};
}

if(plant.length !== 0 && environment['light'] > 6 && life['nutrient'] > 20 && life['water'] > 6){
    plant.forEach(function(stem){
        if(stem.name === 'two'){
            if(stem.form.slice(-1) === '*'){
                result.verb = 'ted';
            }
            else{
                result.verb = 'bloom';
            }
            result.args = {'stemName': 'two'};
        }
    });
}

result;
