import argparse

# As defined in ILSVRC2012_devkit_t12/readme.txt
def loadMetaMat(metaMatPath):
    from scipy.io import loadmat
    meta = loadmat(metaMatPath)
    metaArray = []
    for item in meta['synsets']:
        metaArray.append({
            'ILSVRC2012_ID': item[0][0][0][0],
            'WNID': item[0][1][0],
            'words': item[0][2][0],
            'gloss': item[0][3][0],
            'num_children': item[0][4][0][0],
            'children': item[0][5][0],
            'wordnet_height': item[0][6][0][0],
            'num_train_images': item[0][7][0][0]
            })
    return metaArray

def printExpaneded(item, depth, field, metaArray):
    print(' ' * depth + item[field][:20])
    if item['num_children'] > 0:
        for childId in item['children']:
            childItem = metaArray[childId - 1]
            printExpaneded(childItem, depth + len(item[field][:20]), field, metaArray)

def printItems(items, args, metaArray):
    table_fmt = '{:<13} | {:<9} | {:<40} | {:<40} | {:<12} | {:<20} | {:<14} | {:<5}'
    if args.table:
        print(table_fmt.format('ILSVRC2012_ID', 'WNID', 'words', 'gloss', 'num_children', 'children', 'wordnet_height', 'num_train_images'))
    for item in items:
        if args.verbose:
            print('ILSVRC2012_ID:    %s' % (item['ILSVRC2012_ID']))
            print('WNID:             %s' % (item['WNID']))
            print('words:            %s' % (item['words']))
            print('gloss:            %s' % (item['gloss']))
            print('num_children:     %s' % (item['num_children']))
            print('children:         %s' % (item['children']))
            print('wordnet_height:   %s' % (item['wordnet_height']))
            print('num_train_images: %s' % (item['num_train_images']))
            print('')
        elif args.table:
            print(table_fmt.format(
                item['ILSVRC2012_ID'], 
                item['WNID'], 
                item['words'][:40], 
                item['gloss'][:40], 
                item['num_children'], 
                str(item['children'])[:20], 
                item['wordnet_height'], 
                item['num_train_images']))
        elif args.showField:
            print(item[args.showField])
        elif args.expand:
            printExpaneded(item, 0, args.expand, metaArray)

def filterItems(args, metaArray):
    itemsFound = []
    for item in metaArray:
        if not args.ILSVRC2012_ID in ('*', str(item['ILSVRC2012_ID'])):
            continue
        if not args.WNID in ('*', item['WNID']):
            continue
        if args.words != '*' and (not args.words in item['words']):
            continue
        if args.gloss != '*' and (not args.gloss in item['gloss']):
            continue

        if args.listChildren:
            for childId in item['children']:
                itemsFound.append(metaArray[childId - 1])
        else:
            itemsFound.append(item)
    return itemsFound

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A tool to inspect Synsets of ILSVRC2012')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-verbose', action='store_true', help='display everything')
    group.add_argument('-table', action='store_true', help='display in a table')
    group.add_argument('-showField', help='display selected field only')
    group.add_argument('-expand', help='expand children (display selected field only)')

    parser.add_argument('-ILSVRC2012_ID', default='*', help='''
        'ILSVRC2012_ID' is an integer ID assigned to each synset. All the low
        level synsets are assigned to an ID between 1 and 1000. All the high
        level synsets have ID higher than 1000.
    ''')
    parser.add_argument('-WNID', default='*', help='''
        WNID' is the WordNet ID of a synset. It is used to uniquely identify
        a synset in ImageNet or WordNet.  The tar files for training images
        are named using WNID. Also it is used in naming individual training
        images.
    ''')
    parser.add_argument('-words', default='*', help='''
        Search given text in 'words'
    ''')
    parser.add_argument('-gloss', default='*', help='''
        Search given text in 'gloss'
    ''')
    parser.add_argument('-listChildren', action='store_true', help='''
        list children instead the item
    ''')

    args = parser.parse_args()
    metaArray = loadMetaMat('meta.mat')
    items = filterItems(args, metaArray)
    printItems(items, args, metaArray)