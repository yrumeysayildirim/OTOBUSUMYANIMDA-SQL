# RESEARCH: Collecting data to train the ML model

### PROBLEM

we must collect data from 3 sources (EGOCepte, AYBU OBS, weather API). The collection process should be done with automated pipelines that recollect data periodically. 

### THE 3 PIPELINES

1. AYBU OBS:

    we want to collect data from the obs system to train a model that predicts student density.

    features to collect:

        1. campus location (ws)
        2. course code (ws)
        3. lecturer name (maybe) (ws)
        4. number of students (ws)
        5. Course Faculty (ws)
        6. Department (ws)
        7. Program (ws)
        8. Form of Teaching (face to face, online)  (ws)
        9. course start time (ws)
        10. course end time (ws)
        11. class (first year, second year, etc.) (ws)
        12. recieve (elective, Compulsory) (ws)
        13. classroom (maybe)


        how to get the data:

        1. web scraping:

            how to reach some of this info:

                1. obs login > semester and course operations > course registeration

                2. obs login > general operation > departement time table

                    PROBLEM: only shows the individual students departement and does not show cricital info such as amount of students taking the course

                3. https://obs.aybu.edu.tr/oibs/bologna/index.aspx

                    PRO: contains general info about course info for all departements

                    PROBLEM: does not show cricital info such as amount of students and start and end times. (GG, we are finished)

                4. https://aybuzem.aybu.edu.tr/course/

                    PRO: contains all amount of students for all course in all faculties (WE ARE SO BACK!!), does not need login

                    PROBLEM: no course time table

                    
                CONCLUSION:

                    we will use web scraping to extract the data.we will use a combination of all 3 websites to get the necessary data. we will probably need 3 different scripts, as well as long-term authentication to access the websites (2 need a login). 
        
        2. API:

            seems like the uni doesnt offer an API for the obs.

    CONCERN:

        some students might have 2 classes on the same day. so the model may take them into account when estimating density for the end time of the morning class but in reality they are not leaving. some students may also just not come to class at all.

        SOLUTIONS(?):

            1. take into account if classes are Compulsory or not
            2. find patterns in class attendence
                1. professors may agree to let us view thier class attendance numbers
                2. we can ask students we know in other departements to count the numbers of students that show up to their classes
                3. uni may give us historic attendance data


    CONCERN:

        we dont have historical student density data. so we either have to estimate using unsupervised learning, or if possible, attempt some kind of in uni live data collection, such as:

            1. using a computer vision model to count the number of exiting students (unlikely, the uni probably wont give us access to cameras + time consuming)
            2. WiFi & Bluetooth Tracking (unlikely)
            3. RFID or QR Code Scans (unlikely, no one scan their card to enter anymore)
            4. Manual Counting (Short-Term Data Collection) (likely, but unreliable)
            5. EGO tells us the amount of card payment swipes at the uni station at specific times. (unlikely)

            CONCLUSION (still not decided yet):

                the most likely course of action is to use a unsupervised ML model to group student density based on the data (eg. low density, medium density, high density)

    CONCERN:

        students who live in on-campus dorms. how do we take them into account when predicting density? they may leave the dorm at unexpected times, completely toppling our system.

        SOLUTIONS(?):

            1. maybe the uni can give us dorm entry data??
            2. Manual Counting (Short-Term Data Collection)
            3. is it even our problem if they are not leaving from the uni proper?

    The campus departements:

    1. faculty of islamic studies (html done) (nope)
    2. Faculty of Communication/İletişim Fakültesi(could not find)(i dont think they started dtudying yet since they are not listed on aybuzem)
    3. Faculty of Humanities and Social Sciences (cnf) (get hana to ask someone she knows)
    4. Faculty of Business Administration (html done)
    5. Faculty of Architecture and Fine Arts (cnf)
    6. Faculty of Health Sciences (cnf) (ask hanna sister)
    7. Faculty of Political Sciences (html done)





2. EGOCepte:

    we want to collect bus and station data to train a model on.

    features to collect:

        1. station name
        2. station number
        3. bus number
        4. bus route
        5. bus capacity

    how to get the data:

        1. web scraping:

            does not look good. bad website UI and lack of necessary info

        2. EGO API:

            do not know if API is offered
            
    CONCERN: 
    
        some buses are bigger and have more capacity, how will we take this into account? if we estimated student density needs 4 buses but 3 large buses are enough, the 4th bus would have left the station empty, which goes against the purpose of our project. and if 4 small buses arrive, they may not fit all the students. (data transformation problem, or result display problem)
        
        SOLUTIONS(?): 

            1. there may be a pattern, where 2 large buses leave the station followed by a small one. observe when in uni, ask the drivers in the station, or take the data from EGO if possible.

            2. adjust model recommendation to factor in bus sizes. for example, the estimated student density is high, so send 2 large buses and 2 small buses, or 3 large buses (assuming 1 large bus == 2 small buses) (probably the easier, more feasible and better performant solution)

                NOTE: if we use this solution, we will have the ML model assume all buses are small and then take the prediction and calculate all the different bus combinations and display them all to the user (assuming 1 large bus == 2 small buses)

                example: the density is medium, send:

                    1. 3 small buses
                    2. 1 large bus and 1 small bus
                    3. 2 large buses (low occupancy/Under-utilized)

    CONCERN:

        if there are many stations in route the bus may become crowded with people from outside the uni. (data transformation problem)
        
            1. is that even our problem??? (dont think so)

    CONCERN:

        which bus are the students going to take? do we optimize for one bus (474)

            1. do a survey



3. weather API

    we want to collect weather data that may effect the transportation needs

    features to collect:

        1. weather forecast

    how to get the data:

        1. weather API

    

