# https://seaborn.pydata.org/tutorial/color_palettes.html?highlight=color

# Built-in Themes
# Seaborn has five built-in themes to style its plots: darkgrid, whitegrid, dark, white, and ticks
sns.set_style("darkgrid")


# Scaling Plots
# In order of relative size they are: paper, notebook, talk, and poster
sns.set_context("paper")

## Scaling Fonts and Line Widths
sns.set_context("poster", font_scale = .5, rc={"grid.linewidth": 0.6})

# if you want to override any of these standards, you can use 'sns.set_context' and pass in 
# the parameter 'rc' to target and reset the value of an individual parameter in a dictionary. 


# Commands for Working with Palettes
# Set the palette using the name of a palette:
sns.set_palette("Paired")

# Save a palette to a variable:
palette = sns.color_palette("bright")

# Use palplot and pass in the variable:
sns.palplot(palette)

## Seaborn Default Color Palette
# Seaborn has six variations of its default color palette: deep, muted, pastel, bright, dark, and colorblind.
sns.set_palette("pastel")

### Using Color Brewer Palettes
# https://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3
custom_palette = sns.color_palette("Paired", 9)
sns.palplot(custom_palette)

qualitative_colors = sns.color_palette("Set3", 10)
sns.palplot(qualitative_colors)

### Sequential Palettes
sequential_colors = sns.color_palette("RdPu", 10)
sns.palplot(sequential_colors)

### Diverging Palettes
diverging_colors = sns.color_palette("RdBu", 10)
sns.palplot(diverging_colors)