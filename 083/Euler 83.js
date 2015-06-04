var fs = require('fs');


var c = function( arr ){
  // converts tuple to string id and other way around
  if ( typeof arr === 'string' ){
    return JSON.parse(arr);
  } else{
    return JSON.stringify(arr);
  }
}

var dj = function( startNode, target ){
  // set the target ID we are looking for
  var tarId = c( target );
  var storage = {};

  // Helper arrays to keep track of what is in the network and the proximity
  var inNetwork = [];
  var inProximity = [];

  // Boolean flag for still calculating
  var unsolved = true;

  // public object to expose
  var q = {};

  var mapSurrounding = function( id, cb ){
    // Takes a key and iterates over the surrouning cells if they exist applying a callback.

    var obj = storage[ id ];
    var tuple = c( id );
    var i = tuple[ 0 ];
    var j = tuple[ 1 ];

    var potentialKeys = [
      [ i + 1, j ], // right
      [ i - 1, j ], // left
      [ i, j + 1 ], // up
      [ i, j - 1 ]  // down
    ];

    for (var index = 0; index < potentialKeys.length; index++){
      var newId = c( potentialKeys[ index ] );
      var obj = storage[ newId ];

      if ( obj ){
        cb( obj );
      }

    }
  };

  q.start = function(){
    this.addToNetwork( startNode[ 0 ], startNode[ 1 ]);
    while ( unsolved ){
      var nextNode = this.getMinDist()
      this.addToNetwork( nextNode[0], nextNode[1] )
    }
  };

  q.createNode = function( i, j, dist ){
    // creating a new node object
    var tup = [i,j];
    var id = c( tup );
    var obj = {
      tup: tup,
      i: i,
      j: j,
      dist: dist,
      cDist: Infinity,
      inNetwork: false,
      inProximity: false
    }
    storage[ id ] = obj;
  };

  q.getMinDist = function(){
    // function to get the minimum distance in the proximity nodes
    var distances = inProximity.map( function( id ){
      return storage[id].dist;
    });
    return c( inProximity[ distances.indexOf( Math.min.apply( null, distances ) ) ] );
  };

  q.updateDistance = function( id, cumulativeDistance, updateDistance ){
    // When this function is triggered it means that a shorter distance has been found to a node
    // that is already in the existing network. We need to update the cumulative distance for this node
    // to reflect the lower value, but we also have to check if this update makes any other nodes
    // paths shorter
    var obj = storage[ id ];
    obj.cDist = cumulativeDistance + obj.dist;
    var cDist = obj.cDist;

    // Now that we updated this distance, its possible that there is a shorter path to surroundign nodes
    mapSurrounding( id, function( newObj ){
      if (( newObj.inNetwork || newObj.inProximity ) && (newObj.cDist > cDist + newObj.dist) ){
        updateDistance( c( newObj.tup ) , cDist, updateDistance)
      }
    })
  };

  q.addToNetwork = function( i, j ){
    // function to add a node to the network
    // Getting the id and the object
    var id = c([ i, j ]);
    var obj = storage[ id ];

    // Pushing to network array and triggering network bool
    inNetwork.push(id);
    obj.inNetwork = true;

    // this if statement only needs to be there because the first node added
    // to the network won't be int the proximity.
    if ( inProximity.indexOf( id ) !== -1 ){
      inProximity.splice( inProximity.indexOf( id ), 1 );
    }
    obj.inProximity = false;

    if ( !Number.isFinite( obj.cDist ) ){
      // check to see whether this is the start of a path
      obj.cDist = obj.dist;
    }
    var cDist = obj.cDist;

    if ( id ===  tarId ){
      console.log('ANSWER is' , obj.cDist);
      unsolved = false;
    }


    var potentialKeys = [
      [ i + 1, j ], // right
      [ i - 1, j ], // left
      [ i, j + 1 ], // up
      [ i, j - 1 ]  // down
    ];

    var updateDistance = this.updateDistance;

    potentialKeys.forEach( function( newKey ){
      var newId = c( newKey );

      var obj = storage[ newId ];
      if ( obj ){
        // if this object exists it is in bounds of matrix
        if ( obj.inNetwork || obj.inProximity ){
          // if it is in the network or the proximity already
          if ( obj.cDist > obj.dist + cDist ){
            // a shorter parto to this node has been found
            updateDistance( newId, cDist, updateDistance);
          }
        } else{
          // this index needs to be put into the proximity
          obj.inProximity = true;
          inProximity.push( newId );
          obj.cDist = cDist + obj.dist;
        }
      }
    })
  };

  q.print = function(){
    var retString = '';
    for (var i = 0; i < 80; i++){
      for (var j = 0; j < 80; j++){
        var id = c( [i,j] )
        retString += storage[id].dist + ','
      }
      retString += '\n'
    }
    console.log(retString);
  }

  return q;

}
var data = dj( [ 0, 0 ], [ 79, 79 ] );
var matrix = fs.readFile('matrix.txt', function( err, results ){
  rows = results.toString().split( '\n' ).map( function( row, i ){
    return row.split( ',' ).map( function( num, j ){
      data.createNode( i, j, parseInt( num ));
      return parseInt( num );
    });
  })

  data.start();



});
