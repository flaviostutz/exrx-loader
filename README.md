# exrx-loader

Exrx.net exercise database scrapper.

We tried to get the best of the great structure from the website [Exrx](https://exrx.net) and store it in a relational database, so it can be manipulated and enriched in other applications.

## Design

### Model

<img src="model.png" width="400"/>

Source: https://miro.com/app/board/o9J_l9T9uF8=/

### Scrape path

* Open each MuscleGroup page (ex: https://exrx.net/Lists/ExList/NeckWt)
  * Discover all exercises in MuscleGroup page by url
    * URL format is "/WeightExercises/(muscle_name)/(two_letter_equipment_initials)(exercise_name)"
  * Collect exercise URL, muscle, equipment_initials and exercise_name
  * For each exercise
    * Get from page: display_name, instructions_preparation, instructions_execution, instructions_comments, muscles_target, muscles_synergists, muscles_stabilizers, muscles_dynstabilizers, muscles_antagonist_stabilizers, utility, mechanics, force and video_url
    * Add info URL, exercise_name and equipment_initials from previous step


### Acknowledgments

Based on initial work from https://github.com/cikeddy/SI507_Final

