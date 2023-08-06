import base64
import ipywidgets as widgets
from pathlib import PurePath
from jupyter_bbox_widget import BBoxWidget

if 'google.colab' in str(get_ipython()):
    from google.colab import output
    output.enable_custom_widget_manager()

class Labeler:
    def  __init__(self, dataset=None):
        self.dataset = dataset

    def UseBBoxWidget(self, new_classes=None,image=None):
        """Display the bbox widget loaded with images and annotations from this dataset."""
        dataset = self.dataset
        widget_output = None

        files = dataset.df.img_filename.unique()
        files = files.tolist()

        if image == None:
            file_index = 0
            image = files[0]
        else:
            file_index = files.index(image)

        def GetBBOXs(image):  
            #Make a dataframe with the annotations for a single image
            img_df = dataset.df.loc[dataset.df['img_filename'] == image]
            img_df_subset = img_df[['cat_name','ann_bbox_height','ann_bbox_width','ann_bbox_xmin','ann_bbox_ymin']]
            #Rename the columns to match the format used by jupyter_bbox_widget
            img_df_subset.columns = ['label', 'height', 'width', 'x', 'y']
            #Drop rows that have NaN, invalid bounding boxes
            img_df_subset = img_df_subset.dropna()
            bboxes_dict = img_df_subset.to_dict(orient='records')
            return bboxes_dict

        bboxes_dict = GetBBOXs(image)

        img_folder = dataset.df.loc[dataset.df['img_filename'] == image].iloc[0]["img_folder"]
        file_paths = [str(PurePath(dataset.path_to_annotations, img_folder, file)) for file in files]

        def encode_image(filepath):
            with open(filepath, 'rb') as f:
                image_bytes = f.read()
            encoded = str(base64.b64encode(image_bytes), 'utf-8')
            return "data:image/jpg;base64,"+encoded


        def GetCatId(cat, cat_dict):
            if len(cat_dict)==0:
                cat_id = 0
            elif cat in cat_dict.keys():
                cat_id = cat_dict[cat]
            else:
                #Create a new cat id that 1+ the highest cat id value
                new_cat_id = max([int(v) for v in cat_dict.values()]) + 1
                print(new_cat_id)
                new_cat_id = new_cat_id
                cat_id = cat_dict.setdefault(cat, new_cat_id)
            return cat_id

        def on_submit():
            # save annotations for current image
            import pandas as pd
            global widget_output
            
            widget_output = pd.DataFrame.from_dict(w_bbox.bboxes)
            widget_output = widget_output.rename(columns={"label": "cat_name", "height": "ann_bbox_height", 
                                "width": "ann_bbox_width", "x": "ann_bbox_xmin", "y": "ann_bbox_ymin"})

            img_filename = files[w_progress.value]

            widget_output["img_filename"] = str(img_filename)
            widget_output["img_filename"] = widget_output["img_filename"].astype('string')
            widget_output["cat_name"] = widget_output["cat_name"].astype('string')

            widget_output["ann_area"] = widget_output["ann_bbox_height"] * widget_output["ann_bbox_width"]

            categories  = dict(zip(dataset.df.cat_name, dataset.df.cat_id))

            # for row in widget_output.index:
            #     widget_output['cat_id'][row] = GetCatId(widget_output['cat_name'][row], categories )
            #     widget_output['cat_id'][row] = 1 

            widget_output['cat_id'] = widget_output['cat_name'].map(categories)  
            widget_output.index.name = "id"

            img_df = dataset.df.loc[dataset.df['img_filename'] == img_filename]
            metadata = img_df.iloc[0].to_frame().T
            metadata['img_filename'] = metadata['img_filename'].astype("string")
            metadata.drop(['cat_name', 'cat_id', 'ann_area', 'ann_bbox_height', 'ann_bbox_width', 'ann_bbox_xmin', 'ann_bbox_ymin'], axis=1, inplace=True)
            
            widget_output = widget_output.merge(metadata, left_on='img_filename', right_on='img_filename')
            
            widget_output = widget_output[dataset.df.columns]

            #Now we have a dataframe with output of the bbox widget 
            #Drop the current annotations for the image and add the the new ones
            dataset.df.drop(dataset.df[dataset.df['img_filename'] == image].index, inplace = True)
            dataset.df.reset_index(drop=True, inplace=True)

            dataset.df = dataset.df.append(widget_output).reset_index(drop=True) 

            # move on to the next file
            on_skip()

        def on_skip():
            w_progress.value += 1
            # open new image in the widget
            image_file = file_paths[w_progress.value]
            w_bbox.image = encode_image(image_file)
            # here we assign an empty list to bboxes but 
            # we could also run a detection model on the file
            # and use its output for creating inital bboxes
            w_bbox.bboxes = GetBBOXs(files[w_progress.value]) 


        if new_classes:
            classes = dataset.analyze.classes + new_classes
        else: 
            classes = dataset.analyze.classes 

        #remove empty labels and duplicate labels
        classes = list(set([c.strip() for c in classes if len(c.strip()) > 0]))

        #Load BBoxWidget for first load on page
        w_bbox = BBoxWidget(
            image=encode_image(file_paths[file_index]),
            classes=classes,
            bboxes=bboxes_dict
        )

        w_progress = widgets.IntProgress(value=file_index, max=len(files), description='Progress')

        w_container = widgets.VBox([
            w_progress,
            w_bbox,
        ])

        w_bbox.on_submit(on_submit)
        w_bbox.on_skip(on_skip)

        #Returning the container will show the widgets 
        return w_container
